"""
## LICENSETYPE: Requires license
## MODELTYPE: NLP, MIP, MPEC

Adversarial attack optimization in GAMSPy (MNIST).

Builds and solves a bounded-noise attack that minimizes the logit margin
between the predicted class and runner-up to induce misclassification.
Users control the NN shape (hidden_layers, hidden_layer_neurons) and the
modeling approach: MIP with CPLEX, NLP with CONOPT or MPEC with NLPEC.
Weights are loaded from a pretrained NN (You can either train your own NN to
check for yourself, or use the example file we provide in this repository).

Inputs: a correctly classified MNIST test image; noise ∈ [-MNIST_NOISE_BOUND, +MNIST_NOISE_BOUND].
Outputs: a JSON performance report (objective, time, status, size).

Multi-start: pass `noise_init` to `main(...)`. See the Sobol example at the end
of the file for running many instances with diverse initial points.
"""

import os
import json
import sys
import numpy as np

from pathlib import Path

import gamspy as gp
import torch
import torch.nn as nn
from gamspy.math.matrix import dim
from torchvision import datasets, transforms


def build_network(hidden_layers, hidden_layer_neurons):
    layers = []
    layers.append(nn.Linear(784, hidden_layer_neurons))
    layers.append(nn.ReLU())
    for _ in range(hidden_layers - 1):
        layers.append(nn.Linear(hidden_layer_neurons, hidden_layer_neurons))
        layers.append(nn.ReLU())
    layers.append(nn.Linear(hidden_layer_neurons, 10))

    network = nn.Sequential(*layers)
    network.load_state_dict(
        torch.load(
            Path(__file__).parent / f"ffn_data_{hidden_layers}_{hidden_layer_neurons}.pth", weights_only=True, map_location=torch.device("cpu")
        )
    )
    return network


def get_image(network):
    transform = transforms.Compose([transforms.ToTensor()])
    dataset = datasets.MNIST("data", train=False, download=True, transform=transform)
    test_loader = torch.utils.data.DataLoader(dataset)

    for data, target in test_loader:
        data, target = data, target
        single_image = data[0]
        single_target = target[0]
        single_image = single_image.reshape(single_image.size(0), -1)

        if torch.argmax(network(single_image)) == single_target:
            return single_image


def convert_nlp(m: gp.Container, layer: torch.nn.ReLU):
    return gp.math.relu_with_complementarity_var


def convert_mpec(m: gp.Container, layer: torch.nn.ReLU):
    return gp.math.relu_with_equilibrium


def save_results(report, results_file: str = "performance_report.json") -> None:
    results = []

    if os.path.exists(results_file):
        try:
            with open(results_file, "r") as f:
                data = json.load(f)
                results = data if isinstance(data, list) else [data]
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not read existing results file: {e}")

    results.append(report)

    try:
        with open(results_file, "w") as f:
            json.dump(results, f, indent=2)
    except IOError as e:
        print(f"Error saving results: {e}")


MEAN = (0.1307,)
STD = (0.3081,)
MNIST_NOISE_BOUND = 0.1

problem_type_map = {
    "MIP": [None, "CPLEX"],
    "NLP": [{"ReLU": convert_nlp}, "CONOPT"],
    "MPEC": [{"ReLU": convert_mpec}, "NLPEC"],
}


def main(
    hidden_layers: int,
    hidden_layer_neurons: int,
    prob_type: str,
    noise_init: np.ndarray = None,
) -> float:
    m = gp.Container()
    network = build_network(hidden_layers, hidden_layer_neurons)
    single_image = get_image(network)
    relu_converter, solver = problem_type_map[prob_type]

    image_data = single_image.numpy().reshape(784)

    image = gp.Parameter(
        m, name="image", domain=dim(image_data.shape), records=image_data
    )

    noise = gp.Variable(m, name="noise", domain=dim([784]))
    a1 = gp.Variable(m, name="a1", domain=dim([784]))

    # Set noise bounds
    noise.lo[...] = -MNIST_NOISE_BOUND
    noise.up[...] = MNIST_NOISE_BOUND

    if noise_init is not None:
        noise_vals = gp.Parameter(m, name="noise_vals", domain=noise.domain)
        noise_vals.setRecords(noise_init)
        noise.l[...] = noise_vals[...]

    # set input's lower and upper bounds
    a1.lo[...] = -MEAN[0] / STD[0]
    a1.up[...] = (1 - MEAN[0]) / STD[0]

    set_a1 = gp.Equation(m, "set_a1", domain=dim(a1.shape))
    set_a1[...] = a1 == (image + noise - MEAN[0]) / STD[0]

    matches = {}
    seq_formulation = gp.formulations.TorchSequential(m, network, relu_converter)
    if prob_type.lower() == "mpec":
        y, matches, _ = seq_formulation(a1)
    else:
        y, _ = seq_formulation(a1)

    output_np = network(single_image.unsqueeze(0)).detach().numpy()[0][0]
    right_label = np.argsort(output_np)[-1]
    wrong_label = np.argsort(output_np)[-2]

    obj = gp.Variable(m, name="z")

    margin = gp.Equation(m, "margin")
    margin[...] = obj[...] == y[f"{right_label}"] - y[f"{wrong_label}"]

    model = gp.Model(
        m,
        "min_noise",
        equations=m.getEquations(),
        objective=obj,
        sense="min",
        problem=prob_type,
        matches=matches,
    )

    model.solve(output=sys.stdout, solver=solver, options=gp.Options.fromGams({"reslim": 4000}))

    report = {
        "hidden_layers": hidden_layers,
        "hidden_layer_neurons": hidden_layer_neurons,
        "problem_type": prob_type,
        "objective_value": round(model.objective_value, 5),
        "solve_time": round(model.total_solve_time, 5),
        "status": str(model.status).split(".")[-1],
        "variable_count": model.num_variables,
    }

    save_results(report)

    return model.objective_value


if __name__ == "__main__":
    matches = {}
    obj_value = main(4, 40, prob_type="MPEC")

    # The script below is an example of how to run multiple instances of the model
    # with different hidden layers, hidden layer neurons, and problem types. This
    # can be used as a comprehensive performance evaluation across various configurations.

    # hidden_layers = [1, 2, 3, 4, 5]
    # hidden_layer_neurons = [10, 20, 30, 40, 50, 60]
    # problem_types = ["MIP", "NLP", "MPEC"]
    # for hl in hidden_layers:
    #     for hn in hidden_layer_neurons:
    #         for prob_type in problem_types:
    #             print(f"Running for HL: {hl}, HN: {hn}, Type: {prob_type}")
    #             matches = {}
    #             main(hl, hn, prob_type)
    #             sys.stdout.flush()

    # The script below is an example of how to run multiple instances of the model
    # with different noise initializations sampled via a Sobol sequence.

    # sampler = qmc.Sobol(d=784)              # dimension is the shape of the noise (28x28)
    # samples = sampler.random_base2(m=10)    # Generates 2^10 = 1024 samples
    # scaled_samples = qmc.scale(samples, l_bounds=[-MNIST_NOISE_BOUND]*784, u_bounds=[MNIST_NOISE_BOUND]*784)
    # for sample in scaled_samples:
    #     matches = {}
    #     main(1, 10, prob_type="MPEC", noise_init=sample)
    #     sys.stdout.flush()

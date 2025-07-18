[![GAMSPy](https://github.com/GAMS-dev/gamspy/blob/develop/docs/_static/gamspy_logo.png?raw=true)](https://gamspy.readthedocs.io/en/latest/)

![Tests](https://github.com/GAMS-dev/gamspy-examples/actions/workflows/tests.yml/badge.svg)

## GAMSPy Modeling Examples

This repository contains many examples to show how to model mathematical optimization problems by using [GAMSPy](https://github.com/GAMS-dev/gamspy).
The example models are distributed as either Python script files (under [models](models)) or Jupyter Notebooks (under [notebooks](notebooks)).

## Installing Dependencies

```
git clone git@github.com:GAMS-dev/gamspy-examples.git
pip install -r requirements.txt
```

## Running Locally

```bash
cd <model_directory>
python <model_name>.py
``` 

## Licensing
GAMSPy pip package includes a demo license. For most of the notebooks, this demo license is sufficient. For others, you may need a different license (See [Licensing](https://gams.com/sales/licensing/)). In case you 
already have a GAMSPy license, see [GAMSPy License Installation](https://gamspy.readthedocs.io/en/latest/user/installation.html) guideline.


## List of Models

List of models under `models` directory is listed below. Most models have a GAMS implementation as well for comparison.

| GAMSPy Model                                                  | GAMS Model                                                                                                           | Model Type    | License          |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------- | ---------------- |
| [acopf](models/acopf)                                         |                                                                                                                      | NLP           | Demo             |
| [aircraft](models/aircraft)                                   | [aircraft](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_aircraft.html)                                     | LP            | Demo             |
| [batchreactor](models/batchreactor)                           | [batchreactor](https://www.gams.com/latest/noalib_ml/libhtml/noalib_batchreactor.html)                               | NLP           | Demo             |
| [benz](models/benz)                                           | [benz](https://www.gams.com/latest/noalib_ml/libhtml/noalib_benz.html)                                               | NLP           | Demo             |
| [blend](models/blend)                                         | [blend](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_blend.html)                                           | LP            | Demo             |
| [BondIndex](models/BondIndex)                                 | [BondIndex](https://www.gams.com/latest/finlib_ml/libhtml/finlib_BondIndex.html)                                     | LP            | Demo             |
| [BoundaryLP](models/BoundaryLP)                               | [BoundaryLP](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_BoundaryLP.html)                               | LP            | Demo             |
| [carseq](models/carseq)                                       | [carseq](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_carseq.html)                                         | MIP, MINLP    | Demo             |
| [cesam2](models/cesam2)                                       | [cesam2](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_cesam2.html)                                         | NLP           | Demo             |
| [chain](models/chain)                                         | [chain](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_chain.html)                                           | NLP           | Demo             |
| [chenery](models/chenery)                                     | [chenery](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_chenery.html)                                       | NLP           | Demo             |
| [circuit](models/circuit)                                     | [circuit](https://www.gams.com/latest/noalib_ml/libhtml/noalib_circuit.html)                                         | NLP           | Demo             |
| [clsp](models/clsp)                                           |                                                                                                                      | MIP           | Demo             |
| [coex](models/coex)                                           | [coex](https://www.gams.com/latest/noalib_ml/libhtml/noalib_control3.html)                                           | MIP           | Demo             |
| [control3](models/control3)                                   | [control3](https://www.gams.com/latest/noalib_ml/libhtml/noalib_control3.html)                                       | NLP           | Demo             |
| [Corporate](models/Corporate)                                 | [Corporate](https://www.gams.com/latest/finlib_ml/libhtml/finlib_Corporate.html)                                     | LP            | Requires license |
| [cpa](models/cpa)                                             | [cpa](https://www.gams.com/latest/noalib_ml/libhtml/noalib_cpa.html)                                                 | NLP           | Demo             |
| [cpack](models/cpack)                                         | [cpack](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_cpack.html)                                           | QCP           | Demo             |
| [cta](models/cta)                                             | [cta](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_cta.html)                                               | MIP           | Demo             |
| [cutstock](models/cutstock)                                   | [cutstock](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_cutstock.html)                                     | MIP, RMIP     | Demo             |
| [CVaR](models/CVaR)                                           | [CVaR](https://www.gams.com/latest/finlib_ml/libhtml/finlib_CVaR.html)                                               | LP            | Demo             |
| [dice](models/dice)                                           | [dice](https://gams.com/latest/gamslib_ml/libhtml/gamslib_dice.html)                                                 | MIP           | Demo             |
| [DED](models/DED)                                             | [DED](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_DED.html)                                             | QCP           | Demo             |
| [DED-PB](models/DED-PB)                                       | [DED-PB](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_DED-PB.html)                                       | QCP           | Demo             |
| [DEDESSwind](models/DEDESSwind)                               | [DEDESSwind](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_DEDESSwind.html)                               | QCP           | Demo             |
| [DedicationMip](models/DedicationMip)                         | [DedicationMip](https://www.gams.com/latest/finlib_ml/libhtml/finlib_DedicationMIP.html)                             | LP, MIP       | Demo             |
| [DedicationNoBorrow](models/DedicationNoBorrow)               | [DedicationNoBorrow](https://www.gams.com/latest/finlib_ml/libhtml/finlib_DedicationNoBorrow.html)                   | LP            | Demo             |
| [diffusion2](models/diffusion2)                               |                                                                                                                      | NLP           | Demo             |
| [dyncge](models/dyncge)                                       | [dyncge](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_dyncge.html)                                         | NLP           | Demo             |
| [edc2](models/edc2)                                           | [edc2](https://www.gams.com/latest/noalib_ml/libhtml/noalib_edc2.html)                                               | NLP           | Demo             |
| [EDsensitivity](models/EDsensitivity)                         | [EDsensitivity](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_EDsensitivity.html)                         | QCP           | Demo             |
| [EmergencyCentreAllocation](models/EmergencyCentreAllocation) | [EmergencyCentreAllocation](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_EmergencyCentreAllocation.html) | MIP           | Demo             |
| [EnergyHub](models/EnergyHub)                                 | [EnergyHub](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_EnergyHub.html)                                 | LP            | Demo             |
| [EnvironmentalED](models/EnvironmentalED)                     | [EnvironmentalED](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_EnvironmentalED.html)                     | QCP           | Demo             |
| [fdesign](models/fdesign)                                     | [fdesign](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_fdesign.html)                                       | QCP           | Demo             |
| [fiat](models/fiat)                                           | [fiat](https://www.gams.com/latest/noalib_ml/libhtml/noalib_fiat.html)                                               | NLP           | Demo             |
| [flowshop](models/flowshop)                                   | [flowshop](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_flowshop.html)                                     | MIP           | Demo             |
| [flywheel](models/flywheel)                                   |                                                                                                                      | NLP           | Demo             |
| [food](models/food)                                           | [food](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_food.html)                                             | MIP           | Demo             |
| [fuel](models/fuel)                                           | [fuel](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_fuel.html)                                             | MINLP         | Demo             |
| [gapmin](models/gapmin)                                       | [gapmin](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_gapmin.html)                                         | MIP, RMIP     | Demo             |
| [hansmcp](models/hansmcp)                                     | [hansmcp](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_hansmcp.html)                                       | MCP           | Demo             |
| [hansmge](models/hansmge)                                     | [hansmge](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_hansmge.html)                                       | MCP           | Demo             |
| [heatex3](models/heatex3)                                     | [heatex3](https://www.gams.com/latest/noalib_ml/libhtml/noalib_heatex3.html)                                         | NLP           | Demo             |
| [hhd](models/hhd)                                             |                                                                                                                      | NLP           | Demo             |
| [Horizon](models/Horizon)                                     | [Horizon](https://www.gams.com/latest/finlib_ml/libhtml/finlib_Horizon.html)                                         | LP            | Demo             |
| [Immunization](models/Immunization)                           | [Immunization](https://www.gams.com/latest/finlib_ml/libhtml/finlib_Immunization.html)                               | LP            | Demo             |
| [inscribedsquare](models/inscribedsquare)                     | [inscribedsquare](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_inscribedsquare.html)                       | DNLP          | Demo             |
| [InternationalMeanVar](models/InternationalMeanVar)           | [InternationalMeanVar](https://www.gams.com/latest/finlib_ml/libhtml/finlib_InternationalMeanVar.html)               | NLP           | Demo             |
| [invmat](models/invmat)                                       |                                                                                                                      | LP            | Demo             |
| [iobalance](models/iobalance)                                 | [iobalance](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_iobalance.html)                                   | LP, NLP, QCP  | Demo             |
| [knapsack](models/knapsack)                                   |                                                                                                                      | MIP           | Demo             |
| [korcns](models/korcns)                                       | [korcns](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_korcns.html)                                         | CNS           | Demo             |
| [linear](models/linear)                                       | [linear](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_linear.html)                                         | DNLP, LP, NLP | Demo             |
| [lop](models/lop)                                             | [lop](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_lop.html)                                               | LP, MIP       | Demo             |
| [macro](models/macro)                                         | [macro](https://www.gams.com/latest/noalib_ml/libhtml/noalib_macro.html)                                             | NLP           | Demo             |
| [MAD](models/MAD)                                             | [MAD](https://www.gams.com/latest/finlib_ml/libhtml/finlib_MAD.html)                                                 | LP, NLP       | Demo             |
| [MeanVarMip](models/MeanVarMip)                               | [MeanVarMip](https://www.gams.com/latest/finlib_ml/libhtml/finlib_MeanVarMip.html)                                   | MINLP         | Demo             |
| [mexss](models/mexss)                                         | [mexss](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_mexss.html)                                           | LP            | Demo             |
| [minlphi](models/minlphi)                                     | [minlphi](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_minlphi.html)                                       | MIP, NLP      | Demo             |
| [minlphix](models/minlphix)                                   | [minlphix](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_minlphix.html)                                     | MINLP         | Demo             |
| [MOED](models/MOED)                                           | [MOED](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_MOED.html)                                           | QCP           | Demo             |
| [multiclass_softmax](models/multiclass_softmax)               |                                                                                                                      | NLP           | Demo             |
| [MultiperiodACOPF24bus](models/MultiperiodACOPF24bus)         | [MultiperiodACOPF24bus](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_MultiperiodACOPF24bus.html)         | NLP           | Requires license |
| [nurses](models/nurses)                                       | [nurses](https://gams.com/latest/gamslib_ml/libhtml/gamslib_nurses.html)                                             | MIP           | Demo             |
| [OPF2bus](models/OPF2bus)                                     | [OPF2bus](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_OPF2bus.html)                                     | QCP           | Demo             |
| [OPF5bus](models/OPF5bus)                                     | [OPF5bus](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_OPF5bus.html)                                     | LP            | Demo             |
| [ParetoOptimalFront](models/ParetoOptimalFront)               | [ParetoOptimalFront](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_ParetoOptimalFront.html)               | NLP           | Demo             |
| [partssupply](models/partssupply)                             | [partssupply](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_partssupply.html)                               | NLP           | Demo             |
| [piecewiseLinear](models/piecewiseLinear)                     |                                                                                                                      | MIP           | Requires license |
| [phase](models/phase)                                         |                                                                                                                      | NLP           | Demo             |
| [PMU](models/PMU)                                             | [PMU](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_PMU.html)                                             | MIP           | Demo             |
| [PMU-cost](models/PMU-cost)                                   | [PMU-cost](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_PMU-cost.html)                                   | MIP           | Demo             |
| [PMU-OBI](models/PMU-OBI)                                     | [PMU-OBI](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_PMU-OBI.html)                                     | MIP           | Demo             |
| [poutil](models/poutil)                                       | [poutil](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_poutil.html)                                         | MIP           | Community        |
| [process](models/process)                                     | [process](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_process.html)                                       | NLP           | Demo             |
| [prodmix](models/prodmix)                                     | [prodmix](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_prodmix.html)                                       | LP            | Demo             |
| [protein](models/protein)                                     | [protein](https://www.gams.com/latest/noalib_ml/libhtml/noalib_protein.html)                                         | NLP           | Requires license |
| [ps10_s_mn](models/ps10_s_mn)                                 | [ps10_s_mn](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_ps10_s_mn.html)                                   | NLP           | Demo             |
| [PutCall](models/PutCall)                                     | [PutCall](https://www.gams.com/latest/finlib_ml/libhtml/finlib_PutCall.html)                                         | LP            | Demo             |
| [qdemo7](models/qdemo7)                                       | [qdemo7](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_qdemo7.html)                                         | QCP           | Demo             |
| [qp6](models/qp6)                                             | [qp6](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_qp6.html)                                               | MCP           | Demo             |
| [RampSenDED](models/RampSenDED)                               | [RampSenDED](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_RampSenDED.html)                               | QCP           | Demo             |
| [ramsey](models/ramsey)                                       | [ramsey](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_ramsey.html)                                         | NLP           | Demo             |
| [rcpsp](models/rcpsp)                                         | [rcpsp](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_rcpsp.html)                                           | MIP           | Requires license |
| [refrigeration](models/refrigeration)                         | [refrigeration](https://www.gams.com/latest/noalib_ml/libhtml/noalib_refrigeration.html)                             | NLP           | Demo             |
| [Regret](models/Regret)                                       | [Regret](https://www.gams.com/latest/finlib_ml/libhtml/finlib_Regret.html)                                           | LP            | Demo             |
| [reservoir](models/reservoir)                                 | [reservoir](https://www.gams.com/latest/noalib_ml/libhtml/noalib_reservoir.html)                                     | NLP           | Demo             |
| [reshop](models/reshop)                                       |                                                                                                                      | EMP           | Demo             |
| [riversys](models/riversys)                                   |                                                                                                                      | NLP           | Demo             |
| [robustlp](models/robustlp)                                   | [robustlp](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_robustlp.html)                                     | LP, QCP       | Demo             |
| [rotdk](models/rotdk)                                         | [rotdk](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_rotdk.html)                                           | MIP           | Requires license |
| [sat](models/sat)                                             |                                                                                                                      | MINLP         | Demo             |
| [SelectiveHedging](models/SelectiveHedging)                   | [SelectiveHedging](https://www.gams.com/latest/finlib_ml/libhtml/finlib_SelectiveHedging.html)                       | LP            | Demo             |
| [sgolfer](models/sgolfer)                                     | [sgolfer](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_sgolfer.html)                                       | MINLP, MIP    | Requires license |
| [Sharpe](models/Sharpe)                                       | [Sharpe](https://www.gams.com/latest/finlib_ml/libhtml/finlib_Sharpe.html)                                           | NLP           | Demo             |
| [SimpleLP](models/SimpleLP)                                   | [SimpleLP](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_SimpleLP.html)                                   | LP            | Demo             |
| [SimpleMIP](models/SimpleMIP)                                 | [SimpleMIP](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_SimpleMIP.html)                                 | MIP           | Demo             |
| [spatequ](models/spatequ)                                     | [spatequ](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_spatequ.html)                                       | LP, MCP, NLP  | Demo             |
| [spbenders1](models/spbenders1)                               | [spbenders1](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_spbenders1.html)                                 | LP            | Demo             |
| [speed](models/speed)                                         | [speed](https://www.gams.com/latest/noalib_ml/libhtml/noalib_speed.html)                                             | NLP           | Demo             |
| [springchain](models/springchain)                             | [springchain](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_springchain.html)                               | QCP           | Demo             |
| [StochDedicationBL](models/StochDedicationBL)                 | [StochDedicationBL](https://www.gams.com/latest/finlib_ml/libhtml/finlib_StochDedicationBL.html)                     | LP            | Community        |
| [surface](models/surface)                                     | [surface](https://www.gams.com/latest/noalib_ml/libhtml/noalib_surface.html)                                         | NLP           | Demo             |
| [syscomp](models/syscomp)                                     |                                                                                                                      | LP            | Demo             |
| [tanksize](models/tanksize)                                   | [tanksize](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_tanksize.html)                                     | MINLP         | Demo             |
| [TEP](models/TEP)                                             | [TEP](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_TEP.html)                                             | MIP           | Demo             |
| [tforss](models/tforss)                                       | [tforss](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_tforss.html)                                         | LP            | Demo             |
| [thai](models/thai)                                           | [thai](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_thai.html)                                             | MIP           | Demo             |
| [ThreeStageSPDA](models/ThreeStageSPDA)                       | [ThreeStageSPDA](https://www.gams.com/latest/finlib_ml/libhtml/finlib_ThreeStageSPDA.html)                           | LP, NLP       | Demo             |
| [timesteps](models/timesteps)                                 | [timesteps](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_timesteps.html)                                   | MIP           | Requires license |
| [traffic](models/traffic)                                     | [traffic](https://gams.com/latest/gamslib_ml/libhtml/gamslib_traffic.html)                                           | NLP, MCP      | Requires license |
| [TransportationOn-Off](models/TransportationOn-Off)           | [TransportationOn-Off](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_TransportationOn-Off.html)           | MINLP         | Demo             |
| [trnsport](models/trnsport)                                   | [trnsport](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_trnsport.html)                                     | LP            | Demo             |
| [trnspwl](models/trnspwl)                                     | [trnspwl](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_trnspwl.html)                                       | MIP, NLP      | Demo             |
| [trussm](models/trussm)                                       | [trussm](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_trussm.html)                                         | QCP           | Demo             |
| [tsp](models/tsp)                                             |                                                                                                                      | MIP           | Demo             |
| [tsp4](models/tsp4)                                           | [tsp4](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_tsp4.html)                                             | MIP           | Demo             |
| [WaterEnergy](models/WaterEnergy)                             | [WaterEnergy](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_WaterEnergy.html)                             | MINLP         | Demo             |
| [weapons](models/weapons)                                     | [weapons](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_weapons.html)                                       | NLP           | Demo             |
| [whouse](models/whouse)                                       | [whouse](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_whouse.html)                                         | LP            | Demo             |


All models under notebooks can be run with the demo license. 

[![GAMSPy](https://github.com/GAMS-dev/gamspy/blob/develop/docs/_static/gamspy_logo.png?raw=true)](https://gamspy.readthedocs.io/en/latest/)

## GAMSPy modeling examples

This repository contains many examples to show how to model mathematical optimization problems by using [GAMSPy](https://github.com/GAMS-dev/gamspy).
The example models are distributed as either Python script files (.py) or Jupyter Notebooks (.ıpynb).

## Installing Dependencies

```
pip install gamspy
```

## Run locally

```bash
cd <model_directory>
python <model_name>.py
or
jupyter-lab <model_directory>  # All notebooks can also be run on Google Colab.
``` 

## Licensing
GAMSPy pip package includes a demo license. For most of the notebooks, this demo license is sufficient. For others, you may need a different license (See [Licensing](https://gams.com/sales/licensing/)).


## Index of modeling examples

| GAMSPy Model                                                  | GAMS Model                                                                                                           | Model Type    | License          |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------- | ---------------- |
| [carseq](models/carseq)                                       | Does not exist                                                                                                       | NLP           | Demo             |
| [hansmcp](models/hansmcp)                                     | [aircraft](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_aircraft.html)                                     | LP            | Demo             |
| [hhd](models/hhd)                                             | [batchreactor](https://www.gams.com/latest/noalib_ml/libhtml/noalib_batchreactor.html)                               | NLP           | Demo             |
| [cutstock](models/cutstock)                                   | [benz](https://www.gams.com/latest/noalib_ml/libhtml/noalib_benz.html)                                               | NLP           | Demo             |
| [cpack](models/cpack)                                         | [blend](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_blend.html)                                           | LP            | Demo             |
| [TEP](models/TEP)                                             | [BondIndex](https://www.gams.com/latest/finlib_ml/libhtml/finlib_BondIndex.html)                                     | LP            | Demo             |
| [linear](models/linear)                                       | [BoundaryLP](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_BoundaryLP.html)                               | LP            | Demo             |
| [SimpleLP](models/SimpleLP)                                   | [carseq](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_carseq.html)                                         | MIP, MINLP    | Demo             |
| [qdemo7](models/qdemo7)                                       | [cesam2](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_cesam2.html)                                         | NLP           | Demo             |
| [korcns](models/korcns)                                       | [chain](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_chain.html)                                           | NLP           | Demo             |
| [rotdk](models/rotdk)                                         | [chenery](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_chenery.html)                                       | NLP           | Demo             |
| [minlphix](models/minlphix)                                   | [circuit](https://www.gams.com/latest/noalib_ml/libhtml/noalib_circuit.html)                                         | NLP           | Demo             |
| [tsp4](models/tsp4)                                           | Does not exist                                                                                                       | MIP           | Demo             |
| [food](models/food)                                           | [control3](https://www.gams.com/latest/noalib_ml/libhtml/noalib_control3.html)                                       | NLP           | Demo             |
| [weapons](models/weapons)                                     | [Corporate](https://www.gams.com/latest/finlib_ml/libhtml/finlib_Corporate.html)                                     | LP            | Requires license |
| [Horizon](models/Horizon)                                     | [cpa](https://www.gams.com/latest/noalib_ml/libhtml/noalib_cpa.html)                                                 | NLP           | Demo             |
| [thai](models/thai)                                           | [cpack](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_cpack.html)                                           | QCP           | Demo             |
| [fiat](models/fiat)                                           | [cta](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_cta.html)                                               | MIP           | Demo             |
| [whouse](models/whouse)                                       | [cutstock](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_cutstock.html)                                     | MIP, RMIP     | Demo             |
| [trnspwl](models/trnspwl)                                     | [CVaR](https://www.gams.com/latest/finlib_ml/libhtml/finlib_CVaR.html)                                               | LP            | Demo             |
| [robustlp](models/robustlp)                                   | [DED](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_DED.html)                                             | QCP           | Demo             |
| [chain](models/chain)                                         | [DED-PB](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_DED-PB.html)                                       | QCP           | Demo             |
| [EnergyHub](models/EnergyHub)                                 | [DEDESSwind](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_DEDESSwind.html)                               | QCP           | Demo             |
| [springchain](models/springchain)                             | [DedicationMip](https://www.gams.com/latest/finlib_ml/libhtml/finlib_DedicationMIP.html)                             | LP, MIP       | Demo             |
| [BondIndex](models/BondIndex)                                 | [DedicationNoBorrow](https://www.gams.com/latest/finlib_ml/libhtml/finlib_DedicationNoBorrow.html)                   | LP            | Demo             |
| [invmat](models/invmat)                                       | Does not exist                                                                                                       | NLP           | Demo             |
| [trussm](models/trussm)                                       | [dyncge](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_dyncge.html)                                         | NLP           | Demo             |
| [DedicationNoBorrow](models/DedicationNoBorrow)               | [edc2](https://www.gams.com/latest/noalib_ml/libhtml/noalib_edc2.html)                                               | NLP           | Demo             |
| [lop](models/lop)                                             | [EDsensitivity](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_EDsensitivity.html)                         | QCP           | Demo             |
| [protein](models/protein)                                     | [EmergencyCentreAllocation](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_EmergencyCentreAllocation.html) | MIP           | Demo             |
| [qp6](models/qp6)                                             | [EnergyHub](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_EnergyHub.html)                                 | LP            | Demo             |
| [reservoir](models/reservoir)                                 | [EnvironmentalED](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_EnvironmentalED.html)                     | QCP           | Demo             |
| [partssupply](models/partssupply)                             | [fdesign](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_fdesign.html)                                       | QCP           | Demo             |
| [EnvironmentalED](models/EnvironmentalED)                     | [fiat](https://www.gams.com/latest/noalib_ml/libhtml/noalib_fiat.html)                                               | NLP           | Demo             |
| [EDsensitivity](models/EDsensitivity)                         | [flowshop](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_flowshop.html)                                     | MIP           | Demo             |
| [phase](models/phase)                                         | Does not exist                                                                                                       | NLP           | Demo             |
| [OPF5bus](models/OPF5bus)                                     | [food](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_food.html)                                             | MIP           | Demo             |
| [timesteps](models/timesteps)                                 | [fuel](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_fuel.html)                                             | MINLP         | Demo             |
| [DEDESSwind](models/DEDESSwind)                               | [gapmin](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_gapmin.html)                                         | MIP, RMIP     | Demo             |
| [SimpleMIP](models/SimpleMIP)                                 | [hansmcp](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_hansmcp.html)                                       | MCP           | Demo             |
| [surface](models/surface)                                     | [hansmge](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_hansmge.html)                                       | MCP           | Demo             |
| [OPF2bus](models/OPF2bus)                                     | [heatex3](https://www.gams.com/latest/noalib_ml/libhtml/noalib_heatex3.html)                                         | NLP           | Demo             |
| [clsp](models/clsp)                                           | Does not exist                                                                                                       | NLP           | Demo             |
| [Immunization](models/Immunization)                           | [Horizon](https://www.gams.com/latest/finlib_ml/libhtml/finlib_Horizon.html)                                         | LP            | Demo             |
| [ps10_s_mn](models/ps10_s_mn)                                 | [Immunization](https://www.gams.com/latest/finlib_ml/libhtml/finlib_Immunization.html)                               | LP            | Demo             |
| [MAD](models/MAD)                                             | [inscribedsquare](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_inscribedsquare.html)                       | DNLP          | Demo             |
| [WaterEnergy](models/WaterEnergy)                             | [InternationalMeanVar](https://www.gams.com/latest/finlib_ml/libhtml/finlib_InternationalMeanVar.html)               | NLP           | Demo             |
| [chenery](models/chenery)                                     | Does not exist                                                                                                       | LP            | Demo             |
| [PMU-cost](models/PMU-cost)                                   | [iobalance](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_iobalance.html)                                   | LP, NLP, QCP  | Demo             |
| [spbenders1](models/spbenders1)                               | [korcns](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_korcns.html)                                         | CNS           | Demo             |
| [refrigeration](models/refrigeration)                         | [linear](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_linear.html)                                         | DNLP, LP, NLP | Demo             |
| [InternationalMeanVar](models/InternationalMeanVar)           | [lop](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_lop.html)                                               | LP, MIP       | Demo             |
| [cpa](models/cpa)                                             | [macro](https://www.gams.com/latest/noalib_ml/libhtml/noalib_macro.html)                                             | NLP           | Demo             |
| [circuit](models/circuit)                                     | [MAD](https://www.gams.com/latest/finlib_ml/libhtml/finlib_MAD.html)                                                 | LP, NLP       | Demo             |
| [spatequ](models/spatequ)                                     | [MeanVarMip](https://www.gams.com/latest/finlib_ml/libhtml/finlib_MeanVarMip.html)                                   | MINLP         | Demo             |
| [heatex3](models/heatex3)                                     | [mexss](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_mexss.html)                                           | LP            | Demo             |
| [diffusion2](models/diffusion2)                               | [minlphi](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_minlphi.html)                                       | MIP, NLP      | Demo             |
| [MultiperiodACOPF24bus](models/MultiperiodACOPF24bus)         | [minlphix](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_minlphix.html)                                     | MINLP         | Demo             |
| [nurses](models/nurses)                                       | [MOED](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_MOED.html)                                           | QCP           | Demo             |
| [benz](models/benz)                                           | [MultiperiodACOPF24bus](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_MultiperiodACOPF24bus.html)         | NLP           | Requires license |
| [sgolfer](models/sgolfer)                                     | Does not exist                                                                                                       | MIP           | Demo             |
| [batchreactor](models/batchreactor)                           | [OPF2bus](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_OPF2bus.html)                                     | QCP           | Demo             |
| [fdesign](models/fdesign)                                     | [OPF5bus](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_OPF5bus.html)                                     | LP            | Demo             |
| [acopf](models/acopf)                                         | [ParetoOptimalFront](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_ParetoOptimalFront.html)               | NLP           | Demo             |
| [RampSenDED](models/RampSenDED)                               | [partssupply](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_partssupply.html)                               | NLP           | Demo             |
| [dyncge](models/dyncge)                                       | Does not exist                                                                                                       | NLP           | Demo             |
| [DED-PB](models/DED-PB)                                       | [PMU](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_PMU.html)                                             | MIP           | Demo             |
| [Regret](models/Regret)                                       | [PMU-cost](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_PMU-cost.html)                                   | MIP           | Demo             |
| [prodmix](models/prodmix)                                     | [PMU-OBI](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_PMU-OBI.html)                                     | MIP           | Demo             |
| [trnsport](models/trnsport)                                   | [poutil](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_poutil.html)                                         | MIP           | Community        |
| [cesam2](models/cesam2)                                       | [process](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_process.html)                                       | NLP           | Demo             |
| [CVaR](models/CVaR)                                           | [prodmix](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_prodmix.html)                                       | LP            | Demo             |
| [PMU-OBI](models/PMU-OBI)                                     | [protein](https://www.gams.com/latest/noalib_ml/libhtml/noalib_protein.html)                                         | NLP           | Requires license |
| [SelectiveHedging](models/SelectiveHedging)                   | [ps10_s_mn](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_ps10_s_mn.html)                                   | NLP           | Demo             |
| [rcpsp](models/rcpsp)                                         | [PutCall](https://www.gams.com/latest/finlib_ml/libhtml/finlib_PutCall.html)                                         | LP            | Demo             |
| [Corporate](models/Corporate)                                 | [qdemo7](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_qdemo7.html)                                         | QCP           | Demo             |
| [hansmge](models/hansmge)                                     | [qp6](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_qp6.html)                                               | MCP           | Demo             |
| [speed](models/speed)                                         | [RampSenDED](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_RampSenDED.html)                               | QCP           | Demo             |
| [ParetoOptimalFront](models/ParetoOptimalFront)               | [ramsey](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_ramsey.html)                                         | NLP           | Demo             |
| [blend](models/blend)                                         | [rcpsp](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_rcpsp.html)                                           | MIP           | Requires license |
| [flowshop](models/flowshop)                                   | [refrigeration](https://www.gams.com/latest/noalib_ml/libhtml/noalib_refrigeration.html)                             | NLP           | Demo             |
| [BoundaryLP](models/BoundaryLP)                               | [Regret](https://www.gams.com/latest/finlib_ml/libhtml/finlib_Regret.html)                                           | LP            | Demo             |
| [DED](models/DED)                                             | [reservoir](https://www.gams.com/latest/noalib_ml/libhtml/noalib_reservoir.html)                                     | NLP           | Demo             |
| [process](models/process)                                     | Does not exist                                                                                                       | NLP           | Demo             |
| [macro](models/macro)                                         | [robustlp](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_robustlp.html)                                     | LP, QCP       | Demo             |
| [aircraft](models/aircraft)                                   | [rotdk](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_rotdk.html)                                           | MIP           | Requires license |
| [DedicationMip](models/DedicationMip)                         | [SelectiveHedging](https://www.gams.com/latest/finlib_ml/libhtml/finlib_SelectiveHedging.html)                       | LP            | Demo             |
| [iobalance](models/iobalance)                                 | [sgolfer](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_sgolfer.html)                                       | MINLP, MIP    | Requires license |
| [EmergencyCentreAllocation](models/EmergencyCentreAllocation) | [Sharpe](https://www.gams.com/latest/finlib_ml/libhtml/finlib_Sharpe.html)                                           | NLP           | Demo             |
| [ThreeStageSPDA](models/ThreeStageSPDA)                       | [SimpleLP](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_SimpleLP.html)                                   | LP            | Demo             |
| [inscribedsquare](models/inscribedsquare)                     | [SimpleMIP](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_SimpleMIP.html)                                 | MIP           | Demo             |
| [cta](models/cta)                                             | [spatequ](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_spatequ.html)                                       | LP, MCP, NLP  | Demo             |
| [PMU](models/PMU)                                             | [spbenders1](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_spbenders1.html)                                 | LP            | Demo             |
| [fuel](models/fuel)                                           | [speed](https://www.gams.com/latest/noalib_ml/libhtml/noalib_speed.html)                                             | NLP           | Demo             |
| [flywheel](models/flywheel)                                   | [springchain](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_springchain.html)                               | QCP           | Demo             |
| [MeanVarMip](models/MeanVarMip)                               | [StochDedicationBL](https://www.gams.com/latest/finlib_ml/libhtml/finlib_StochDedicationBL.html)                     | LP            | Community        |
| [tanksize](models/tanksize)                                   | [surface](https://www.gams.com/latest/noalib_ml/libhtml/noalib_surface.html)                                         | NLP           | Demo             |
| [control3](models/control3)                                   | Does not exist                                                                                                       | LP            | Demo             |
| [MOED](models/MOED)                                           | [tanksize](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_tanksize.html)                                     | MINLP         | Demo             |
| [poutil](models/poutil)                                       | [TEP](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_TEP.html)                                             | MIP           | Demo             |
| [syscomp](models/syscomp)                                     | [tforss](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_tforss.html)                                         | LP            | Demo             |
| [gapmin](models/gapmin)                                       | [thai](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_thai.html)                                             | MIP           | Demo             |
| [TransportationOn-Off](models/TransportationOn-Off)           | [ThreeStageSPDA](https://www.gams.com/latest/finlib_ml/libhtml/finlib_ThreeStageSPDA.html)                           | LP, NLP       | Demo             |
| [Sharpe](models/Sharpe)                                       | [timesteps](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_timesteps.html)                                   | MIP           | Requires license |
| [ramsey](models/ramsey)                                       | [TransportationOn-Off](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_TransportationOn-Off.html)           | MINLP         | Demo             |
| [tforss](models/tforss)                                       | [trnsport](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_trnsport.html)                                     | LP            | Demo             |
| [PutCall](models/PutCall)                                     | [trnspwl](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_trnspwl.html)                                       | MIP, NLP      | Demo             |
| [minlphi](models/minlphi)                                     | [trussm](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_trussm.html)                                         | QCP           | Demo             |
| [StochDedicationBL](models/StochDedicationBL)                 | [tsp4](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_tsp4.html)                                             | MIP           | Demo             |
| [edc2](models/edc2)                                           | [WaterEnergy](https://www.gams.com/latest/psoptlib_ml/libhtml/psoptlib_WaterEnergy.html)                             | MINLP         | Demo             |
| [riversys](models/riversys)                                   | [weapons](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_weapons.html)                                       | NLP           | Demo             |
| [mexss](models/mexss)                                         | [whouse](https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_whouse.html)                                         | LP            | Demo             |

#!/bin/bash

python gru_onehot_time.py data/2_1_outpatient_De_V_Di_M_S.p.seqs.ll data/2_1_outpatient_De_V_Di_M_S.p.times.ll data/2_1_outpatient_De_V_Di_M_S.p.labels results/2_1_outpatient_De_V_Di_M_S_hidden_256.result_subset_.4_iter_1 570 0.4 256
python gru_onehot_time.py data/2_1_outpatient_De_V_Di_M_S.p.seqs.ll data/2_1_outpatient_De_V_Di_M_S.p.times.ll data/2_1_outpatient_De_V_Di_M_S.p.labels results/2_1_outpatient_De_V_Di_M_S_hidden_256.result_subset_.4_iter_2 570 0.4 256
python gru_onehot_time.py data/2_1_outpatient_De_V_Di_M_S.p.seqs.ll data/2_1_outpatient_De_V_Di_M_S.p.times.ll data/2_1_outpatient_De_V_Di_M_S.p.labels results/2_1_outpatient_De_V_Di_M_S_hidden_256.result_subset_.4_iter_3 570 0.4 256
python gru_onehot_time.py data/2_1_outpatient_De_V_Di_M_S.p.seqs.ll data/2_1_outpatient_De_V_Di_M_S.p.times.ll data/2_1_outpatient_De_V_Di_M_S.p.labels results/2_1_outpatient_De_V_Di_M_S_hidden_256.result_subset_.4_iter_4 570 0.4 256
python gru_onehot_time.py data/2_1_outpatient_De_V_Di_M_S.p.seqs.ll data/2_1_outpatient_De_V_Di_M_S.p.times.ll data/2_1_outpatient_De_V_Di_M_S.p.labels results/2_1_outpatient_De_V_Di_M_S_hidden_256.result_subset_.4_iter_5 570 0.4 256


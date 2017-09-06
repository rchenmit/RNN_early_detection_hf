## convert list of list of list to [list of list + list of times ]

import numpy as np
import cPickle as pickle

file_lll_seqs = 'data/2_1_outpatient_social_DISCRETE.p.seqs'
file_l_labels = 'data/2_1_outpatient_social_DISCRETE.p.labels'
file_save_ll_seqs_new = 'data/2_1_outpatient_social_DISCRETE.p.seqs.ll'
file_save_ll_t_new = 'data/2_1_outpatient_social_DISCRETE.p.times.ll'


with open(file_lll_seqs, 'rb') as f:
	lll_seqs = pickle.load(f)
f.close()

with open(file_l_labels, 'rb') as f:
	l_labels = pickle.load(f)
f.close()

ll_seqs_new = []
ll_times = []

cnt = 0
for ll in lll_seqs:
	cnt += 1
	if np.mod(cnt, 100) ==0:
		print cnt

	l_new = []
	l_t = []
	t = 0
	for l in ll:
		l_new += l
		for i in range(len(l)):
			l_t.append(t)
		t += 1
	ll_seqs_new.append(l_new)
	ll_times.append(l_t)



pickle.dump(ll_seqs_new, open(file_save_ll_seqs_new, 'wb'))
pickle.dump(ll_times, open(file_save_ll_t_new, 'wb'))

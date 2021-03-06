## convert list of list of list to [list of list + list of times ]

import numpy as np
import cPickle as pickle

file_lll_seqs = 'data/2_1_outpatient_De_V_Di_M_S_enc_cutoff_25.p.seqs'
file_l_labels = 'data/2_1_outpatient_De_V_Di_M_S_enc_cutoff_25.p.labels'
file_save_ll_seqs_new = 'data/2_1_outpatient_De_V_Di_M_S_enc_cutoff_25.p.seqs.ll'
file_save_ll_t_new = 'data/2_1_outpatient_De_V_Di_M_S_enc_cutoff_25.p.times.ll'


with open(file_lll_seqs, 'rb') as f:
	lll_seqs = pickle.load(f)
f.close()

with open(file_l_labels, 'rb') as f:
	l_labels = pickle.load(f)
f.close()





ll_seqs_new = []
ll_times = []

for ll in lll_seqs:
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



#pickle.dump(ll_seqs_new, open(file_save_ll_seqs_new, 'wb'))
#pickle.dump(ll_times, open(file_save_ll_t_new, 'wb'))


## make subsets (keep same ratio of case and control)

### find which ones are case (1) and which control (0)
nparr_labels = np.array(l_labels)
l_labels_0 = np.where(nparr_labels==0)[0]
l_labels_1 = np.where(nparr_labels==1)[0]
print l_labels_1

num_pts_total = int(len(l_labels))
num_pts_0 = int(len(l_labels_0))
num_pts_1 = int(len(l_labels_1))

print "num patients 0: ", num_pts_0
print "num patients 1: ", num_pts_1

#l_pcts_pick = [ 0.02, 0.035, 0.1, 0.2, 0.3,0.4,0.5,0.6,0.7,0.8,0.9, 1]
l_pcts_pick = [  1]

for pct in l_pcts_pick:
	num_pick_0 = int(np.floor(pct * num_pts_0))
	num_pick_1 = int( np.floor(pct * num_pts_1))

        num_pick_total = int(np.floor(pct * num_pts_total))


        l_times_this = []
        l_seqs_this = []
        l_labels_new = []

        for p in range(num_pick_total):
                l_times_this.append(ll_times[p])
                l_seqs_this.append(ll_seqs_new[p])
                l_labels_new.append(l_labels[p])

	# new save filenames
	seqs_this_save_name = file_save_ll_seqs_new + '.subset_' + str(pct)
	times_this_save_name = file_save_ll_t_new + '.subset_' + str(pct)
        labels_this_save_name = file_l_labels + '.subset_' + str(pct)

	# dump pickles
	pickle.dump(ll_seqs_new, open(seqs_this_save_name, 'wb'))
	pickle.dump(ll_times, open(times_this_save_name, 'wb'))
	pickle.dump(l_labels_new, open(labels_this_save_name, 'wb'))
        





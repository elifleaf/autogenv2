import sys
sys.path.append("../")

import pickle as pkl

with open('plan.pickle','rb') as inpf:
  plan=pkl.load(inpf)

plan.nextstep()

print("\n\n\n###############################-- Summary \n")
print(plan.generate_report())

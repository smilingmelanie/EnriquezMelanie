import random

Cardinality = 2
NumberTrials = 100
p = 0.50
TrialSequence = []
for TrialIndex in range(0, NumberTrials):
	if random.random() < p:
		TrialSequence.append(1)
	else:
		TrialSequence.append(0)

EmpiricalDistribution = []
for OutcomeIndex in range (0 , Cardinality) :
	EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution


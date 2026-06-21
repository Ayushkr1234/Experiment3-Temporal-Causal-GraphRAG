from collections import defaultdict

attack_sequences = [
    ["Initial Access", "Execution", "Persistence"],
    ["Initial Access", "Execution", "Persistence"],
    ["Execution", "Persistence", "Discovery"],
    ["Execution", "Persistence", "Collection"],
    ["Execution", "Persistence", "Exfiltration"],
]

transitions = defaultdict(lambda: defaultdict(int))

for sequence in attack_sequences:

    for i in range(len(sequence)-1):

        current = sequence[i]
        nxt = sequence[i+1]

        transitions[current][nxt] += 1

current_state = "Persistence"

next_states = transitions[current_state]

prediction = max(
    next_states,
    key=next_states.get
)

print("Current State:", current_state)
print("Predicted Next Tactic:", prediction)

print("\nTransition Counts:")

for state,count in next_states.items():
    print(state,":",count)
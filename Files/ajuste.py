input_file = "placzek_12k_a_28-Jan_lift.txt"
output_file = "placzek_12k_a_28-Jan_lift_out.txt"

with open(input_file, "r") as fin, open(output_file, "w") as fout:
    for i, line in enumerate(fin):
        if i % 10 == 0:   # keep every 10th line
            fout.write(line)

from ansible_runner import Runner, RunnerConfig
import subprocess

# Running the playbook with ansible_runner
rc = RunnerConfig(
    private_data_dir="./",
    playbook="hello.yml"
)
rc.prepare()
r = Runner(config=rc)
r.run()

# Run the curl command three times and print the output. Break if actual and expected output do not match.
for i in range(1, 4):
    result = subprocess.run(["curl", "http://0.0.0.0"], capture_output=True, text=True)
    print(f"Output from curl request {i}:")
    expected_output =  f"Hello World from managedhost-app-{i} !"
    print(result.stdout)
    if result.stdout != expected_output:
        print(f"FAIL: Expected \n{expected_output}")
        break
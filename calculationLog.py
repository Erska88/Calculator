
import pandas as pd

# init log file
log_file_path = "calculation_log.csv"
if not pd.io.common.file_exists(log_file_path):
    df = pd.DataFrame(columns=["calculation", "result"])
    df.to_csv(log_file_path, index=False)

def log_calculation(calculation: str, result: float):
    #print(f"Calculation: {calculation} = {result}")
    log_file = pd.read_csv(log_file_path)
    new_record = {"calculation": calculation, "result": result}
    log_file = pd.concat([log_file, pd.DataFrame([new_record])], ignore_index=True)
    log_file.to_csv(log_file_path, index=False)
    


    






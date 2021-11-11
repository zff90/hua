from AnsaProcessModule import AnsaProcess

ANSA_EXE = "c:\\Program Files (x86)\\BETA_CAE_Systems\\ansa_v22.0.0\\ansa64.bat"

def main():
    process = AnsaProcess(ansa_command=ANSA_EXE, run_in_batch=False)
    connection = process.get_iap_connection()
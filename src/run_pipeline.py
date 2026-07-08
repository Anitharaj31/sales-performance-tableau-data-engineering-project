import subprocess
from logger import logger


logger.info("========== PIPELINE STARTED ==========")

try:

    subprocess.run(
        ["python3", "src/ingestion.py"],
        check=True
    )

    subprocess.run(
        ["python3", "src/transformation.py"],
        check=True
    )

    subprocess.run(
        ["python3", "src/data_quality.py"],
        check=True
    )

    subprocess.run(
        ["python3", "src/load_to_mysql.py"],
        check=True
    )


    logger.info("========== PIPELINE COMPLETED SUCCESSFULLY ==========")

    print("ETL Pipeline Completed Successfully")


except Exception as e:

    logger.error(
        f"Pipeline Failed: {e}"
    )

    print("Pipeline Failed")

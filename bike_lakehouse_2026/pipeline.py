# Upgrade Databricks SDK to the latest version and restart Python to see updated packages
%pip install --upgrade databricks-sdk==0.70.0
%restart_python

from databricks.sdk.service.jobs import JobSettings as Job


bike_lakehouse_2026 = Job.from_dict(
    {
        "name": "bike_lakehouse_2026",
        "trigger": {
            "pause_status": "UNPAUSED",
            "periodic": {
                "interval": 1,
                "unit": "DAYS",
            },
        },
        "tasks": [
            {
                "task_key": "bronze_layer",
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/vladimirvukojicic@gmail.com/databricks_bootcamp_2026/bike_lakehouse_2026/bronze/bronze(improved)",
                    "source": "WORKSPACE",
                },
            },
            {
                "task_key": "silver_layer",
                "depends_on": [
                    {
                        "task_key": "bronze_layer",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/vladimirvukojicic@gmail.com/databricks_bootcamp_2026/bike_lakehouse_2026/silver/silver_orchestration",
                    "source": "WORKSPACE",
                },
            },
            {
                "task_key": "gold_layer",
                "depends_on": [
                    {
                        "task_key": "silver_layer",
                    },
                ],
                "notebook_task": {
                    "notebook_path": "/Workspace/Users/vladimirvukojicic@gmail.com/databricks_bootcamp_2026/bike_lakehouse_2026/gold/gold_orchestration",
                    "source": "WORKSPACE",
                },
            },
        ],
        "queue": {
            "enabled": True,
        },
        "performance_target": "PERFORMANCE_OPTIMIZED",
    }
)

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
w.jobs.reset(new_settings=bike_lakehouse_2026, job_id=803209181019808)
# or create a new job using: w.jobs.create(**bike_lakehouse_2026.as_shallow_dict())


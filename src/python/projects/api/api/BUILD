python_sources(
    interpreter_constraints=["==3.11.*"],
    dependencies=[
        "src/python/projects/api:req",
        "src/python/libs/common/visionguard:common",

        "src/python/projects/api:files"
    ],
    resolve="project_api",
)
pex_binary(
    interpreter_constraints=["==3.11.*"],
    name="main",
    entry_point="main.py",
    restartable=True,
    resolve="project_api",
)

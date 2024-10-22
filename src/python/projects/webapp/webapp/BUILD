python_sources(
    interpreter_constraints=["==3.11.*"],
    dependencies=[
        "src/python/projects/webapp:req",


        "src/python/projects/webapp:files"
    ],
    resolve="project_webapp",
)
pex_binary(
    interpreter_constraints=["==3.11.*"],
    name="main",
    entry_point="main.py",
    restartable=True,
    resolve="project_webapp",
)

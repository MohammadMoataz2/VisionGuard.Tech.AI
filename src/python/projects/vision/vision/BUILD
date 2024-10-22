python_sources(
    interpreter_constraints=["==3.11.*"],
    dependencies=[
        "src/python/projects/vision:req",


        "src/python/projects/vision:files"
    ],
    resolve="project_vision",
)
pex_binary(
    interpreter_constraints=["==3.11.*"],
    name="main",
    entry_point="main.py",
    restartable=True,
    resolve="project_vision",
)

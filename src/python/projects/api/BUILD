resources(name="files", sources=["./**/*"])

docker_image(
    name="visionguard-tech-api",
    dependencies=[":files", "src/python/projects/api/api:main"],
    registries=[
        "mohammadmoataz777",
    ],
    image_tags=["0.0.2"],
)

python_requirements(source="requirements.txt", name="req", resolve="project_api")

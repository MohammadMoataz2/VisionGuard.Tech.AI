resources(name="files", sources=["./**/*"])

docker_image(
    name="visionguard-tech-webapp",
    dependencies=[":files", "src/python/projects/webapp/webapp:main"],
    registries=[
        "mohammadmoataz777",
    ],
    image_tags=["0.0.1"],
)

python_requirements(source="requirements.txt", name="req", resolve="project_webapp")

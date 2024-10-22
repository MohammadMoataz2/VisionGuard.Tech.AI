resources(name="vision_files", sources=["./**/*"])

docker_image(
    name="visionguard-tech-vision",
    dependencies=[":vision_files", "src/python/projects/vision/vision:main"],
    registries=[
        "mohammadmoataz777",
    ],
    image_tags=["0.0.1"],
)
python_requirements(source="requirements.txt", name="req", resolve="project_vision")

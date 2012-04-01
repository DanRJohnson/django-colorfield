from setuptools import setup, find_packages

setup(
    name = "django-colorfield",
    version = "0.0.1",
    author = "Jared Forsyth, Dan Johnson, Marco Bonetti",
    author_email = "mbonetti@gmail.com",
    description = "a small app providing a colorpicker field for django",
    license = "BSD",
    keywords = "django color picker",
    url = "https://github.com/mbi/django-colorfield",
    packages=find_packages(),
    long_description="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    include_package_data=True,
    zip_safe=False
)

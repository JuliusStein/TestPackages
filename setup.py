import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-AudioModuleTest",
    version="1.1",
    author="Ryan Soklaski (@rsokl)",
    author_email="ry26099@mit.edu",
    description="Provides simple interface for recording audio",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        pyaudio,
        ipython,
        jupyter,
        notebook,
        numpy,
        scipy,
        matplotlib,
        numba,
        librosa,
        ffmpeg,
        mygrad
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)

try:
    import pyaudio
except ImportError:
      print("Warning: `pyaudio` must be installed in order to use `microphone`")

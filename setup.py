from setuptools import setup

setup(
    name="pwython",
    version="dev",
    description="A meme error handler for python",
    author="Systematic Error",
    url="https://github.com/SystematicError/Pwython",
    packages=["pwython"],
    entry_points={
        "console_scripts": [
            "pwython = pwython.__main__",
        ]
    }
)

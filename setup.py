from setuptools import setup

setup(
    name="pwython",
    version="1.0.0",
    description="A meme error handler for python",
    author="Systematic Error",
    url="https://github.com/SystematicError/Pwython",
    packages=["pwython"],
    entry_points={
        "console_scripts": [
            "pwython = pwython.__main__:main",
        ]
    }
)

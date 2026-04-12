"""Setup for email-triage-env package."""

from setuptools import setup, find_packages

setup(
    name="email-triage-env",
    version="1.0.0",
    description="Email triage RL environment with task grading",
    author="OpenEnv",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "pydantic",
        "fastapi",
        "uvicorn",
        "openai",
    ],
    entry_points={
        "console_scripts": [
        ],
    },
)

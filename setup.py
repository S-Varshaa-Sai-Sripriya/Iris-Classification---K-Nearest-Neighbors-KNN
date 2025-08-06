from setuptools import setup, find_packages

setup(
    name='knn_iris_classifier',
    version='0.1.0',
    author='Varshaa Sai Sripriya Saisheshadhri',
    description='K-Nearest Neighbors classifier for the Iris dataset with structured ML pipeline',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'matplotlib',
        'seaborn',
        'jupyter',
        'pyyaml'
    ],
    entry_points={
        'console_scripts': [
            'train-model=src.model.trainer:main'
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)

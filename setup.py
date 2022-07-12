import setuptools

setuptools.setup(name="vault-lib", 
                version="1.0", 
                description="A SDK to interact with VAULT infastructure, and a requirement for all vault tools",
                url="https://github.com/stevezaluk/vault-lib",
                install_requires=["pymongo", "plexapi", "colorama", "requests"],
                python_requires='>=3')
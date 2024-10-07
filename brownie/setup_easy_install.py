from setuptools.command.easy_install import easy_install

def install_dependency_via_git(git_url):
    installer = easy_install(None)  # None means no specific distribution
    installer.args = [git_url]      # The package or git URL to install
    installer.ensure_finalized()    # Finalize the installation
    installer.run()                 # Run the installation

# Example usage: Installing from a Git URL
install_dependency_via_git('git+https://github.com/user/repo.git#egg=package_name')

from setuptools import setup, find_namespace_packages

setup(
    name="FriendlyHandbook_kobSK",
    version="0.1.8",
    description="«FriendlyHandbook» - це корисна програма з інтерфейсом командного рядка, яка містить все необхідне",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown; charset=UTF-8; variant=GFM",
    author="Sasha Kuspys",
    url="https://github.com/SashaKuspys/homework_1-web-",
    author_email="sashakuspys@gmail.com",
    license="MIT",
    packages=find_namespace_packages(),
    entry_points={"console_scripts": ["assistant_bot=FriendlyHandbook_kobSK.main:assistant_bot"]},
)

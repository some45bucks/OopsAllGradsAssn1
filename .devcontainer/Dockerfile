FROM ros:iron-ros-base
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID ros \
    && useradd --uid $USER_UID --gid $USER_GID -m ros -d /home/ros \
    && apt-get update \
    && apt-get install -y sudo \
    && echo ros ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/ros \
    && chmod 0440 /etc/sudoers.d/ros
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3-pip neovim
ENV SHELL /bin/bash

# ********************************************************
# * Anything else you want to do like clean up goes here *
# ********************************************************

# [Optional] Set the default user. Omit if you want to keep the default as root.
USER ros
CMD ["/bin/bash"]
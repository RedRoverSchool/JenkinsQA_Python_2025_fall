FROM jenkins/jenkins:2.516.3

USER root

# Plugin Manager Tool
RUN curl -L \
  https://github.com/jenkinsci/plugin-installation-manager-tool/releases/download/2.13.2/jenkins-plugin-manager-2.13.2.jar \
  -o /usr/share/jenkins/plugin-manager.jar

COPY plugins.txt /usr/share/jenkins/plugins.txt

# Install plugins
RUN java -jar /usr/share/jenkins/plugin-manager.jar \
    --plugin-file /usr/share/jenkins/plugins.txt \
    --plugin-download-directory /usr/share/jenkins/ref/plugins \
    --verbose

USER jenkins
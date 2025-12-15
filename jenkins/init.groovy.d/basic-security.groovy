// import jenkins.model.*
// import hudson.security.*
//
// def instance = Jenkins.get()
//
// println ">>> Running security setup..."
//
// def user = System.getenv("JENKINS_USERNAME")
// def pass = System.getenv("JENKINS_PASSWORD")
//
// println ">>> Creating admin user: ${user}"
//
// def realm = new HudsonPrivateSecurityRealm(false)
// if (realm.getUser(user) == null) {
//     realm.createAccount(user, pass)
// }
// instance.setSecurityRealm(realm)
//
// def strategy = new FullControlOnceLoggedInAuthorizationStrategy()
// strategy.setAllowAnonymousRead(false)
// instance.setAuthorizationStrategy(strategy)
//
// instance.save()
//
// println ">>> Security configured."

import jenkins.model.*
import hudson.security.*
import jenkins.security.ApiTokenProperty
import hudson.model.User

def instance = Jenkins.get()

def username = System.getenv("JENKINS_USERNAME")
def password = System.getenv("JENKINS_PASSWORD")

println ">>> Running security setup..."
println ">>> Creating admin user: ${username}"

// --- Security realm ---
def realm = new HudsonPrivateSecurityRealm(false)
instance.setSecurityRealm(realm)

def user = realm.getUser(username)
if (user == null) {
    user = realm.createAccount(username, password)
}

// --- Authorization ---
def strategy = new FullControlOnceLoggedInAuthorizationStrategy()
strategy.setAllowAnonymousRead(false)
instance.setAuthorizationStrategy(strategy)

// --- API TOKEN ---
def apiTokenProperty = user.getProperty(ApiTokenProperty.class)

if (apiTokenProperty == null) {
    apiTokenProperty = new ApiTokenProperty()
    user.addProperty(apiTokenProperty)
}

def token = apiTokenProperty.tokenStore.generateNewToken("ephemeral-tests-token")

new File("/var/jenkins_home/api-token").text = token.plainValue

user.save()
instance.save()

println "==== JENKINS API TOKEN CREATED ===="

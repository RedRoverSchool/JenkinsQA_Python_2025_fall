import jenkins.model.*
import hudson.security.*

def instance = Jenkins.get()

println ">>> Running security setup..."

def user = System.getenv("JENKINS_USERNAME")
def pass = System.getenv("JENKINS_PASSWORD")

println ">>> Creating admin user: ${user}"

def realm = new HudsonPrivateSecurityRealm(false)
if (realm.getUser(user) == null) {
    realm.createAccount(user, pass)
}
instance.setSecurityRealm(realm)

def strategy = new FullControlOnceLoggedInAuthorizationStrategy()
strategy.setAllowAnonymousRead(false)
instance.setAuthorizationStrategy(strategy)

instance.save()

println ">>> Security configured."

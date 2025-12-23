def create_user_script(username, password, full_name, email):
    groovy_script = f"""
                    import jenkins.model.*
                    import hudson.security.*
                    import hudson.model.*
                    import hudson.tasks.Mailer

                    def instance = Jenkins.get()
                    def realm = instance.getSecurityRealm()

                    if (!(realm instanceof HudsonPrivateSecurityRealm)) {{
                        throw new RuntimeException("Not Jenkins own user database")
                    }}

                    def username = "{username}"
                    def userPassword = "{password}"
                    def fullName = "{full_name}"
                    def email = "{email}"

                    // создать пользователя, если нет
                    def user = realm.getUser(username)
                    if (user == null) {{
                        user = realm.createAccount(username, userPassword)
                    }}

                    // обновить профиль
                    user.setFullName(fullName)
                    user.addProperty(new Mailer.UserProperty(email))

                    user.save()
                    instance.save()

                    println "User ready: ${{username}}"
                    """
    return groovy_script


def delete_user_script(username):
    groovy_script = f"""
            import hudson.model.*

            def user = User.get("{username}", false)
            if (user != null) {{
                user.delete()
                println "User deleted: {username}"
            }} else {{
                println "User not found: {username}"
            }}
            """
    return groovy_script
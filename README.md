# bad-secrets

Repository with potential secrets here and there. The repository could be used to test different tools to scan different types of potential secrets.

## Tools

### GitHub Enterprise Security Secret Scanning

If your project communicates with an external service, you might use a token or private key for authentication. Tokens and private keys are examples of secrets that a service provider can issue. If you check a secret into a repository, anyone who has read access to the repository can use the secret to access the external service with your privileges. We recommend that you store secrets in a dedicated, secure location outside of the repository for your project.

Secret scanning will scan your entire Git history on all branches present in your GitHub repository for secrets, even if the repository is archived. Secret scanning also analyzes issue descriptions and comments for secrets.

#### Secret scanning is available on GitHub.com in two forms:

1. Secret scanning alerts for partners. Runs automatically on all public repositories. Any strings that match patterns that were provided by secret scanning partners are reported directly to the relevant partner. For more information, see the ["About secret scanning alerts for partners"](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/about-secret-scanning#about-secret-scanning-alerts-for-partners) section.
2. Secret scanning alerts for users. You can enable and configure additional scanning for repositories owned by organizations that use GitHub Enterprise Cloud and have a license for GitHub Advanced Security. This includes private and internal repositories. Any strings that match patterns provided by secret scanning partners, by other service providers, or defined by you or your organization, are reported as alerts in the "Security" tab of repositories. If a string in a public repository matches a partner pattern, it is also reported to the partner. For more information, see the ["About secret scanning alerts for users"](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/about-secret-scanning#about-secret-scanning-alerts-for-users) section.

#### Notes

- [Supported secrets for partner alert](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/secret-scanning-patterns#supported-secrets-for-partner-alerts).
- [Supported secrets for user alert](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/secret-scanning-patterns#supported-secrets-for-user-alerts)
- [Secret scanning partner program](https://docs.github.com/en/enterprise-cloud@latest/developers/overview/secret-scanning-partner-program)
- [Define custom patterns](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning).
- [Excluding directories from secret scanning alerts for users](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/configuring-secret-scanning-for-your-repositories#excluding-directories-from-secret-scanning-alerts-for-users)
- [Protecting pushes with secret scanning](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/protecting-pushes-with-secret-scanning)
  - **Beta** at the time of writing this.

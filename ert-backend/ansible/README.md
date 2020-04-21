- Create a file named `env.yaml` taking reference from the template file `env-template.yaml`

- This file is required to mirror all the secrets mentioned in `./project/config/settings/secrets.json`

- Also, the ansible playbook to deploy drf `drf-playbook.yaml` requires to pull `ert-backend` source code from bitbucket.org using ssh tunnel. Therefore, make sure the machine which is running the playbook has its public ssh-key registered on bitbucket

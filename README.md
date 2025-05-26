# A simple CI/CD
This repository serves an example on how to have a CI/CD to deploy your services to a k8s cluster.
Github Action will do the following upon PR opening:
- Set up KinD cluster
- Set up Traefik for the ingress controller
- Deploy two sample echo services (foo and bar)
- Port-forward traefik to port 8080 and run load test using locust to foo and bar service
- Post the load test result as a comment in the PR

# Time
- 26th May 13.20 - 14:56:
  - Github Action for the CI created with this scope:
    - Setup KinD cluster
    - Deployed traefik as ingress controller
    - Deployed foo and bar services
    - Verify the IngressRoute (foo.localhost and bar.localhost)
    - PRs:
      - https://github.com/akbargumbira/ci_cd/pull/1 
      - https://github.com/akbargumbira/ci_cd/pull/2
- 26th May 15:16 - 
# A simple CI/CD
This repository serves an example on how to have a CI/CD to deploy your services to a k8s cluster.
Github Action will do the following upon PR opening:
- Provision KinD cluster with 2 nodes (1 for the control plane, 1 for the worker) (see `kind/cluster-config.yaml`)
- Set up Traefik for the ingress controller
- Deploy two sample echo services (foo and bar) and route (see `k8s/charts` and `k8s/deployment`: 
  - foo.localhost to foo service
  - bar.localhost to bar service
- Port-forward traefik to port 8080 and run load test using locust to foo and bar service
  - Github runner doesn't allow using host port 80 and map it to the container, so traefik is port-forwarded to port 8080
  - Load test is run to both foo and bar services with different header
  - Load test is run with this instruction (see `load_test/locustfile.py`):
    - Run for 30s
    - Ramped up up to 100 users as a target max concurrent users
    - With user spawning rate of 10 users per seconds
    - Subsequent request of a user will randomly wait from 0-1s after a sucessfull response
- Post the load test result as a comment in the PR

# Timeline
- 26th May 13.20 - 14:56:
  - Github Action for the CI created with this scope:
    - Setup KinD cluster
    - Deployed traefik as ingress controller
    - Deployed foo and bar services
    - Verify the IngressRoute (foo.localhost and bar.localhost)
    - PRs:
      - https://github.com/akbargumbira/ci_cd/pull/1 
      - https://github.com/akbargumbira/ci_cd/pull/2
- 26th May 15:16 - 16:28
  - Add load test with locust
  - Post load test result as Github comment
  - PR: https://github.com/akbargumbira/ci_cd/pull/3
# ORAM
This is a project that simulates the Oblivious RAM.

Data encryption schemes are commonly used to prevent unauthorized access to sensitive information. However, attackers can still gain access to information by tracking the access pattern to memory. For example, frequently accessed memory addresses may contain important data. This access pattern threat can compromise encrypted data, as attackers can exploit the information obtained from the access pattern. Figure below represents the threat model and it can help illustrate the significance of this threat.

Oblivious RAM (ORAM) is designed to conceal the access pattern from potential attackers. It has been utilized in both cloud and processor environments. One approach to achieve this is by adding extra memory accesses for each access, which makes it difficult for attackers to extract information from the access pattern or detect the exact address that has been accessed. There are various implementations of ORAM, including a trivial solution that accesses the entire address range, retrieves the required data, and stores back the entire memory, which is inefficient. Another solution, proposed by Stefanov, et al [1], is tree-based ORAM. 
Tree-based ORAM considers the memory address range as a tree and retrieves the entire path from a leaf to the root of the tree for each access. The requested data is located within this path, which is then provided to the CPU for the required access. The entire path is then stored back to the memory, which conceals the accessed address from potential attackers. The primary goal of ORAM is to ensure that each pair of sequenced accesses are hidden, which helps to maintain the confidentiality and security of sensitive information.

<img width="800" alt="image" src="https://github.com/BelalJahannia/ORAM/assets/46157467/bf5e7264-9174-4707-b8b9-e2200107c1a4">



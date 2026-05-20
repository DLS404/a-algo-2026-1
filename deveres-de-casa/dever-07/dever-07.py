import heapq
import random


# =========================
# Classe do Paciente
# =========================
class Paciente:
    def __init__(self, nome, dor):
        self.nome = nome
        self.dor = dor

    def __repr__(self):
        return f"{self.nome} (Dor: {self.dor})"


# =========================
# Classe da Triagem Hospitalar
# =========================
class TriagemHospitalar:
    def __init__(self):
        self.heap = []

    # Inserir paciente
    # Complexidade: O(log N)
    def adicionar_paciente(self, paciente):
        heapq.heappush(
            self.heap,
            (-paciente.dor, id(paciente), paciente)
        )

        print(f"Paciente adicionado: {paciente}")

    # Atender paciente mais urgente
    # Complexidade: O(log N)
    def atender_paciente(self):
        if not self.heap:
            print("Nenhum paciente na fila.")
            return None

        prioridade, _, paciente = heapq.heappop(self.heap)

        print(f"Atendendo: {paciente}")
        return paciente

    # Mostrar fila
    # Complexidade: O(N)
    def mostrar_fila(self):
        print("\nFila atual:")

        for prioridade, _, paciente in sorted(self.heap):
            print(f"- {paciente}")

    # Alterar prioridade
    # Complexidade: O(N)
    def alterar_prioridade(self, nome, nova_dor):
        encontrado = False

        for i in range(len(self.heap)):
            prioridade, identificador, paciente = self.heap[i]

            if paciente.nome == nome:
                encontrado = True

                print(f"\nAlterando prioridade de {paciente.nome}")
                print(f"Dor antiga: {paciente.dor}")
                print(f"Nova dor: {nova_dor}")

                # Remove o paciente
                self.heap[i] = self.heap[-1]
                self.heap.pop()

                # Reorganiza heap
                heapq.heapify(self.heap)

                # Atualiza prioridade
                paciente.dor = nova_dor

                # Reinserir
                heapq.heappush(
                    self.heap,
                    (-paciente.dor, id(paciente), paciente)
                )

                print("Prioridade atualizada!")
                break

        if not encontrado:
            print("Paciente não encontrado.")


# =========================
# Simulação
# =========================
triagem = TriagemHospitalar()

nomes = ["Ana", "Carlos", "Maria", "João", "Fernanda"]

for nome in nomes:
    dor = random.randint(1, 10)
    triagem.adicionar_paciente(Paciente(nome, dor))

triagem.mostrar_fila()

# Alterar prioridade
triagem.alterar_prioridade("Carlos", 10)

triagem.mostrar_fila()

# Atendimento
print("\n=== Atendimento ===")

while triagem.heap:
    triagem.atender_paciente()


# =========================
# Complexidade
# =========================
print("\n=== Complexidade ===")
print("Inserção: O(log N)")
print("Remoção: O(log N)")
print("Alterar prioridade: O(N)")
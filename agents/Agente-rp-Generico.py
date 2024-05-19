class agenteResolucaoDeProblemas(self, Ambiente):
    estado = Ambiente.getEstado()
    objetivo = NULL

    def decidirAcao(self, Ambiente):
        if sequencia == 0:
            objetivo = formularObjetivo(Ambiente.getEstado())
            problema = formularProblema(Ambiente.getEstado(), objetivo)
            sequencia = busca(problema)
        acao = primeiro(sequencia)
        sequencia = resto(sequencia)

        return acao
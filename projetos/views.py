from django.shortcuts import render

# Create your views here.
def projetos(request):
    return render(request, 'projetos/index.html')
def dev (request):
    projetos = [
            {
                "pagina": "detalheDes6",
                "percentual": 90,
                "titulo": "Aplicativo móvel TRE/RN Sociedade",
                "imagem": "img/projetos/dev/appSociedade.png",
                "descricao": "Desenvolvimento de um aplicativo móvel destinado a melhorar a comunicação entre o TRE-RN e o público externo (eleitores, candidatos, professores, imprensa, magistrado, mesário, partido, alunos, advogados, etc.)."
            },
            {
                "pagina": "detalheDes1",
                "percentual": 100,
                "titulo": "Aplicativo móvel Servidor JE",
                "imagem": "img/projetos/dev/appServidorJE.png",
                "descricao": "Desenvolvimento de um aplicativo móvel com funcionalidades úteis e destinado aos servidores, estagiários, residentes e terceirizados do TRE-RN, de modo a melhorar o processo interno de comunicação institucional."
            },
            {
                "pagina": "detalheDes2",
                "percentual": 100,
                "titulo": "Sistema de Comunicação Institucional",
                "imagem": "img/projetos/dev/comunicacaoInstitucional.png",
                "descricao": "O Sistema de Comunicação Institucional consistirá em um sistema Web utilizado no âmbito do TRE-RN, e destinado a ser um canal de comunicação entre o Tribunal e os usuários do aplicativo móvel Servidor JE, a saber, servidores, estagiários, residentes e terceirizados, e os usuários do aplicativo móvel JE Sociedade."
            },
            {
                "pagina": "detalheDes3",
                "percentual": 100,
                "titulo": "Robô de Atendimento - Chatbot para o 77º Encontro do COPTREL",
                "imagem": "img/projetos/dev/roboDeAtendimento.png",
                "descricao": "A proposta deste projeto foi demonstrar o uso de chatbots no 77º Encontro do COPTREL."
            },
            {
                "pagina": "detalheDes5",
                "percentual": 90,
                "titulo": "Robô de Atendimento - Chatbot para os Eleitores",
                "imagem": "img/projetos/dev/roboDeEleitores.png",
                "descricao": "A proposta deste projeto é desenvolver um robô inteligente (Chatbot) que irá tirar dúvidas dos eleitores de forma similar a um servidor de uma Zona Eleitoral, ou seja, irá prestar os esclarecimentos cartorários demandados, tanto de forma geral como personalizada. Desta forma, o eleitor terá a oportunidade de tirar suas dúvidas a qualquer hora do dia, mesmo nos finais de semana. O robô também se integrará a bases de dados e outros sistemas em uso no âmbito do TRE-RN, como por exemplo, os sistemas ELO e Agendamento. A proposta é prestar o atendimento inicial ao eleitor, e caso necessário, encaminhá-lo ao Cartório Eleitoral mediante atendimento agendado."
            },
            {
                "pagina": "detalheDes7",
                "percentual": 90,
                "titulo": "Robô de Atendimento - Chatbot ativo para o acompanhamento de processos judiciais",
                "imagem": "img/projetos/dev/roboDeEleitores.png",
                "descricao": "A proposta deste projeto é informar ao advogado a movimentação de processos e enviar menagem para seu Facebook Messenger."
            }
        ]
    return render(request, 'projetos/dev.html',{'projetos':projetos})
def infra (request):
    projetos = [
            {
                "pagina": "detalheInfra1",
                "percentual": 100,
                "titulo": "Servidor de imagens",
                "descricao": "Servidor de imagens para instalação remota de sistemas operacionais"
            },
            {
                "pagina": "detalheInfra2",
                "percentual": 100,
                "titulo": "Segurança de Rede Cabeada TRE-RN",
                "descricao": "Implementação de mecanismo de autenticação na rede cabeada no TRE-RN (Padrão IEEE 802.1x)"
            },
            {
                "pagina": "detalheInfra3",
                "percentual": 100,
                "titulo": "Melhoria de Wifi TRE-RN",
                "descricao": "Otimização da rede WIFI do prédio administrativo do TRE-RN e disponibilização de Wi-Fi nos cartórios do interior."
            },
            {
                "pagina": "detalheInfra4",
                "percentual": 100,
                "titulo": "Melhoria de Rede Cabeada TRE-RN",
                "descricao": "Verificação e otimização da rede cabeada do prédio administrativo do TRE-RN"
            },
            {
                "pagina": "detalheInfra5",
                "percentual": 100,
                "titulo": "Dashboards Integradas ao GLPI",
                "descricao": "Dashboards no Grafana com informações sobre ativos de redes, com alertas e Integração com sistema de chamados GLPI."
            },
            {
                "pagina": "detalheInfra7",
                "percentual": 100,
                "titulo": "Gerência de Logs TRE-RN",
                "descricao": "Gerência centralizada de logs"
            },
            {
                "pagina": "detalheInfra8",
                "percentual": 100,
                "titulo": "Análise de Logs TRE-RN",
                "descricao": "Análise e Monitoramento Avançado de Logs "
            },
            {
                "pagina": "detalheInfra9",
                "percentual": 100,
                "titulo": "Mapeamento dos ativos de rede com Zabbix",
                "descricao": "Mapeamento dos ativos de rede com Zabbix com alertas no rocket.chat"
            }
        ]
    return render(request, 'projetos/infra.html',{'projetos':projetos})
def business (request):
    projetos= [
            {
                "pagina": "detalheBi1",
                "percentual": 100,
                "imagem": "img/projetos/bi/biOrcamento.png",
                "titulo": "Inteligência de dados aplicada à área de Administração, Orçamento e Finanças",
                "descricao": "Portal web com dashboards contendo dados estatísticos relacionados à área de Administração e Orçamento do TRE-RN, com acesso às bases de dados dos principais sistemas orçamentários, possibilitando a realização de consultas analíticas."
            },
            {
                "pagina": "detalheBi3",
                "percentual": 100,
                "imagem": "img/projetos/bi/cadastroEleitoral.png",
                "titulo": "Inteligência de dados aplicada ao Cadastro Eleitoral",
                "descricao": "Portal web com dashboards contendo dados relativos aos eleitores cadastrados na base eleitoral do TSE, possibilitando a realização de consultas analíticas."
            },
            {
                "pagina": "detalheBi2",
                "percentual": 100,
                "imagem": "img/projetos/bi/gestaoDePessoas.png",
                "titulo": "Inteligência de dados aplicada à área de Gestão de Pessoas",
                "descricao": "Portal web com dashboards contendo dados estatísticos relacionados à área de pessoal do TRE-RN, com acesso às bases de dados do SGRH, Folha de Pagamento, GESTCOM e PAE, possibilitando a realização de consultas analíticas."
            },
            {
                "pagina": "detalheBi4",
                "percentual": 90,
                "imagem": "img/projetos/bi/biJudiciaria.png",
                "titulo": "Inteligência de dados aplicada à área Judiciária",
                "descricao": "Portal web com dashboards contendo dados estatísticos relacionados à área judiciária do TRE-RN, com acesso às bases de dados do SADP e PJE, possibilitando a realização de consultas analíticas."
            },
            {
                "pagina": "detalheBi7",
                "percentual": 100,
                "imagem": "img/projetos/bi/justicaEmNumeros.png",
                "titulo": "Inteligência de dados aplicada à área de Planejamento Estratégico",
                "descricao": "Portal web com dashboards contendo dados estatísticos relacionados à área de Planejamento Estratégico do TRE-RN, possibilitando a realização de consultas analíticas."
            },
            {
                "pagina": "detalheBi5",
                "percentual": 100,
                "imagem": "img/projetos/bi/biEleicoes.png",
                "titulo": "Inteligência de dados aplicada aos Logs das Eleições",
                "descricao": "Portal web com dashboards contendo dados sobre os resultados das eleições a partir de 1945 até os dias atuais, além de dados relacionados aos logs das urnas eletrônicas e do Sistema Gerenciamento, do TSE. "
            },
            {
                "pagina": "detalheBi6",
                "percentual": 100,
                "imagem": "img/projetos/bi/justicaEmNumeros.png",
                "titulo": "Painel de acompanhamento de solicitações de atendimento remoto",
                "descricao": "Portal web com dashboards contendo dados estatísticos relacionados ao atendimento remoto."
            }
        ]
    return render(request, 'projetos/bi.html',{'projetos':projetos})


    
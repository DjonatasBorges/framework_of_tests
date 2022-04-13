from configparser import ConfigParser

from pages.checkbox import Checkbox

config = ConfigParser()
config.read('behave.ini')

APPLICATION_URL = config['behave.userdata']['page']

TEXT_INDEXES = {
    'primeiro': 0,
    'primeira': 0,
    'segundo': 1,
    'segunda': 1,
    'terceiro': 2,
    'terceira': 2
}


PROFILES = {
    "sensedata": "1",
    "admin": "2",
    "csm": "3",
    "cs": "4",
    "viewer": "5",
    "sales": "6",
    "executive": "7"
}


USERS = {
    'admin': {
        'email': 'adminqaauto@sensedata.com.br',
        'password': '$ensed@ta!'
    },
    'cs': {
        'email': 'csqaauto@sensedata.com.br',
        'password': '$ensed@ta!'
    },
    'viewer': {
        'email': 'viewerqaauto@sensedata.com.br',
        'password': '$ensed@ta!'
    },
    'csm': {
        'email': 'csmqaauto@sensedata.com.br',
        'password': '$ensed@ta!'
    },
    'sensedata': {
        'email': 'sensedata@sensedata.com.br',
        'password': '$ensed@ta!'
    }
}

PAGE_OBJECTS = {
    'Checkboxes': Checkbox,

    # TODO: Implement remaining page objects.
    'tarefas': None,
    'onboarding (tabela)': None,
    'relatórios': None,
    'análise da carteira': None,
    'consolidado 360': None,
    'performance de equipe': None,
    'análise de resultados': None,
    'analytics': None,
    'painel executivo': None,
    'painel cs': None,
    'painel cs ops': None,
    'painel sd (padrão)': None
}

URL_SUFFIXES = {
    'minha carteira': 'portfolio',
    'tabela de clientes': 'clientes_new',
    'financeiro': 'billing',
    'configurações da regra': ('nova', '2'),
    'regras individuais': 'regras_individuais',
    'campos customizados': 'custom_fields',
    'template playbook': ('playbooks', 'onboarding_playbooks'),
    'atividades (360)': '1',
    'onboarding': 'onboarding',
    'onboarding (kanban)': 'onboarding_kanban',
    'deletar cliente': 'delete_customer',
    'perfis': 'profiles',
    'atividades': 'customers_task_table',
    'configuração de cards': 'cards',
    'contratos': 'contracts',
    'categorias': 'custom_task_categories',
    'tipos de atividades': 'custom_tasks',
    'suporte': 'support',
    'nps': 'nps',
    'regras terceiros': 'regras_terceiros',
    'indicadores': 'engajamento',
    'configurações de farois': 'farois'
}

MAPPING_DB_ACTIONS = {
    "atividades": {
        "Concluir": "finish_task",
        "Criar": "create_task",
        "Deletar": "delete_task",
        "Editar": "update_task",
        "Editar Concluida": "edit_finished_task"
    },
    "carteira": {
        "Filtrar Indicadores por Usuário": "filter_portfolio_by_team"
    },
    "playbooks": {
        "Concluir": "finish_playbook",
        "Criar": "create_playbook",
        "Deletar": "delete_playbook",
        "Alterar progresso": "progress_playbook",
        "Editar": "edit_playbook"
    },
    "regras": {
        "Alertas": "rule_alert",
        "Atividade": "rule_task_create",
        "Atualização": "rule_customer_update",
        "Distribuição automática": "rule_customer_cs_caster",
        "Email": "rule_email",
        "Playbook": "rule_playbook",
        "SMS": "rule_sms",
        "Webhook": "rule_webhook"
    },
    "clientes": {
        "Adicionar/Editar": "add_and_edit_customer",
        "Adicionar Arquivo": "add_file",
        "Adicionar Nota": "add_note",
        "Alterar Campo Comum": "update_field",
        "Alterar CS": "update_cs_field",
        "Alterar CSM": "update_csm_field",
        "Alterar Campo Restrito": "update_custom_field_restricted",
        "Alterar Campo Customizado": "update_custom_field",
        "Alterar Status": "update_status_field",
        "Deletar Arquivo": "delete_file",
        "Deletar Nota": "delete_note",
        "Apagar Clientes": "delete_customer",
        "Ignorar Alertas": "ignore_alert",
        "Copiar Email": "copy_email",
        "Editar Nota": "edit_note"
    },
    "contatos": {
        "Adicionar Contato": "add_contact",
        "Alterar Contato": "update_contact",
        "Deletar Contato": "delete_contact"
    },
    "contratos": {
        "Adicionar": "add_contract",
        "Editar": "edit_contract",
        "Deletar": "delete_contract"
    },
    "editar analytics": {
        "Painel Executivo": "executive_analytics_edit",
        "Painel CS": "cs_analytics_edit",
        "Painel CS Ops": "csops_analytics_edit"
    },
    "relatorios": {
        "Exportar Clientes": "export_customers",
        "Exportar Atividades": "export_tasks",
        "Exportar Cards Visao 360": "export_360_cards",
        "Exportar Suporte": "export_support",
        "Exportar NPS": "export_nps",
        "Exportar Financeiro": "export_billing",
        "Exportar Contatos": "export_contacts",
        "Exportar Contratos": "export_contracts",
        "Exportar Onboarding": "export_onboarding",
        "Exportar Estatisticas de Email": "export_email_statistics",
        "Exportar Informacoes da Regra": "export_rule_informations"
    }
}

MAPPING_DB_MENUS = {
    "analytics": {
        "Painel Executivo": "executive_analytics",
        "Painel CS": "cs_analytics",
        "Painel CS Ops": "csops_analytics",
        "Painel SD (Padrão)": "default_analytics"
    },
    "apps": {
        "Slack (Webhook)": "config_slack",
        "Voip (Zenvia)": "config_voip",
    },
    "atividades": {
        "Categorias": "config_custom_task_categories",
        "Onboarding Playbooks": "config_onboarding_playbooks",
        "Playbooks": "config_playbooks",
        "Tipos de Atividades": "config_custom_tasks"
    },
    "cs ops": {
        "Medidas Customizadas": "config_custom_data"
    },
    "clientes": {
        "Apagar Clientes": "config_delete_customer",
        "Campos Customizados": "custom_fields_config",
        "Cards Minha Carteira": "config_cards_portfolio_charts",
        "Visão 360": "config_cards_charts",
        "Manutenção via CSV": "config_importing_csv",
        "Motivos de Cancelamento": "config_cancel_reasons",
        "Status dos Clientes": "config_customer_status",
        "Status dos Contratos": "config_contract_status",
        "Status Financeiro": "config_billing_status",
        "Tipos de Contatos": "config_contact_types",
        "Transferir Dados": "config_transfer_data"
    },
    "contas": {
        "Perfis": "config_profiles",
        "Usuários": "config_users"
    },
    "email": {
        "Autenticação de Envio": "config_sender_authentication",
        "Email SPF": "config_emailspf",
        "Lista de envio": "config_email_lists",
        "Templates de Email": "config_email_template_list"
    },
    "indicadores": {
        "Engagement": "config_engagement",
        "Faróis": "config_signals",
        "Sense Score": "config_sensescore"
    },
    "regras": {
        "Regras Gerais": "config_rules",
        "Regras Individuais": "config_restricted_rules",
        "Regras Individuais de Terceiros": "config_third_party_rules"
    },
    "tabelas": {
        "Clientes": "customers_table",
        "Contratos": "contracts_table",
        "Financeiro": "billings_table",
        "Lista de Contatos": "contacts_table",
        "NPS": "nps_table",
        "Onboarding": "onboarding_table",
        "Suporte": "support_table"
    },
    "telas": {
        "Atividades": "tasks_table",
        "Calendário": "calendar_page",
        "Onboarding": "onboarding_page",
        "Performance da Equipe": "team_performance_report"
    }
}
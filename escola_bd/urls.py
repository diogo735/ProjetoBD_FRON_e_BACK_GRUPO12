from django.contrib import admin
from django.urls import path
from app_escola import views  # Importa as views do app
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  
    path('login/', views.login_view, name='login'),
    path('loading/', views.loading_page, name='loading_page'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    #opções da nav bar
 
    path('aluno/dashboard/', views.dashboard_aluno, name='dashboard_aluno'),
    path('professor/dashboard/', views.dashboard_professor, name='dashboard_professor'),
    path('funcionario/dashboard/', views.dashboard_funcionario, name='dashboard_funcionario'),
    path('obter_cursos/', views.obter_cursos, name='obter_cursos'),
    path('obter_ucs/', views.obter_ucs, name='obter_ucs'),
    path('obter_nomes_turnos/', views.obter_nomes_turnos, name='obter_nomes_turnos'),
    path('obter_anos/', views.obter_anos, name='obter_anos'),
    path('obter_semestres/', views.obter_semestres, name='obter_semestres'),
    path('criar_turno/', views.criar_turno, name='criar_turno'),
    path('buscar_dados/', views.buscar_turnos, name='buscar_turnos'),
    path('atualizar_turno/', views.atualizar_turno_view, name='atualizar_turno'),
    path('obter_detalhes_turno/<int:turno_id>/', views.obter_detalhes_turno, name='obter_detalhes_turno'),
    path('verificar_eliminar_turno/', views.verificar_eliminar_turno, name='verificar_eliminar_turno'),
    path('eliminar_turno/', views.eliminar_turno, name='eliminar_turno'),
    path('pesquisar_horarios/', views.pesquisar_horarios, name='pesquisar_horarios'),
    path('obter_horarios_e_ucs/<int:turno_id>/<int:curso_id>/<str:ano>/<str:semestre>/', views.obter_horarios_e_ucs,name='obter_horarios_e_ucs'),
    path('obter_alunos_turno/<int:id_turno>/', views.obter_alunos_turno, name='obter_alunos_turno'),
    path('remover_alunos_turno/', views.remover_alunos_turno, name='remover_alunos_turno'),
    path('obter_id_curso/<str:nome_curso>/', views.obter_id_curso, name='obter_id_curso'),
    path('adicionar_aluno_turno/', views.adicionar_aluno_turno, name='adicionar_aluno_turno'),
    path('obter_turnos_sem_horarios/', views.obter_turnos_sem_horarios, name='obter_turnos_sem_horarios'),
    path('espacos_disponiveis/', views.espacos_disponiveis, name='espacos_disponiveis'),
    path('adicionar_horario/', views.adicionar_horario, name='adicionar_horario'),
    path('obter_turnos/', views.obter_turnos_nomes, name='obter_turnos'),
    path('pesquisar_horarios_filtrados/', views.pesquisar_horarios_filtrados, name='pesquisar_horarios_filtrados'),
    path('obter_horario/<int:horario_id>/', views.obter_horario_detalhes, name='obter_horario'),
    path('editar_horario/<int:id_horario>/', views.atualizar_horario, name='atualizar_horario'),
    path('remover_horario/<int:id_horario>/', views.remover_horario, name='remover_horario'),
    path('carregar_horario_professor/', views.carregar_professor_horario, name='carregar_horario_professor'),
    path('carregar_horario_aluno/', views.carregar_horario_aluno, name='carregar_horario_aluno'),

    path('aluno/horarios/', views.horarios_aluno, name='horarios_aluno'),
    path('professor/horarios/', views.horarios_professor, name='horarios_professor'),

    path('aluno/professores/', views.professores_aluno, name='professores_aluno'),
    path('funcionario/professores/', views.professores_funcionario, name='professores_funcionario'),
    path('funcionarios/professores/remover/<int:id_professor>/', views.professor_delete, name='professor_delete'),
    path('funcionario/professores/editar/<int:id_professor>/', views.professor_editar, name='professor_editar'),
    path('funcionario/professores/atribuirUC/<int:id_professor>/', views.atribuir_uc_professor, name='atribuir_uc_professor'),
    path('funcionario/listar_turnos/<int:id_uc>/', views.listar_turnos_por_uc, name='listar_turnos_por_uc'),
    path("funcionario/registrar_professor_turno/", views.registrar_professor_turno, name="registrar_professor_turno"),
    path('funcionario/remover_uc_professor/', views.remover_atribuicao_uc_professor, name='remover_uc_professor'),
  

    path('aluno/avaliacoes/', views.avaliacoes_aluno, name='avaliacoes_aluno'),
    path('professor/avaliacoes/', views.avaliacoes_professor, name='avaliacoes_professor'),
    path('funcionario/avaliacoes/', views.avaliacoes_funcionario, name='avaliacoes_funcionario'),
    path('avaliacoes/aprovar/<int:id_avaliacao>/', views.aprovar_avaliacao, name='aprovar_avaliacao'),
    path('professor/editar_avaliacao/', views.editar_avaliacao, name='editar_avaliacao'),
    path('funcionario/professores_nao_atribuidos/', views.professores_nao_atribuidos, name='professores_nao_atribuidos'),
    path('funcionario/professores_atribuidos/', views.professores_atribuidos, name='professores_atribuidos'),
    path('funcionario/listar_unidades_curriculares/', views.listar_unidades_curriculares, name='listar_unidades_curriculares'),
    path('aluno/pagamentos/', views.pagamentos_em_falta_alunos, name='pagamentos_aluno'),
    path('aluno_alterar_status_pagamento/<int:id_pagamento>/', views.aluno_alterar_status_pagamento, name='aluno_alterar_status_pagamento'),
    path('funcionario/pagamentos/', views.funcionario_listar_pagamentos, name='pagamentos_funcionario'),
    path('funcionario_alterar_status_pagamento/<int:id_pagamento>/', views.funcionario_alterar_status_pagamento, name='funcionario_alterar_status_pagamento'),
    path('aluno/matricula/', views.matricula_aluno, name='matricula_aluno'),
    path('get_cursos/', views.get_cursos, name='get_cursos'),
    path('get_ucs/<int:curso_id>/<int:ano_id>/', views.get_ucs, name='get_ucs'),
    path('get_turnos/<int:uc_id>/', views.get_turnos, name='get_turnos'),
    path('funcionario/matricula/', views.listar_matriculas, name='matricula_funcionario'),

    path('funcionario/matricula/detalhes/<int:id_matricula>/', views.matricula_detalhes, name='matricula_detalhes'),
    path('funcionario/matricula/update_detalhes/<int:id_matricula>/', views.matricula_atualizar_detalhes, name='matricula_detalhes'),
    path('funcionario/matricula/atualizar/', views.funcionario_atualizar_matricula, name='funcionario_atualizar_matricula'),

    path("funcionario/cursos/", views.get_cursos, name="funcionario_get_cursos"),
    path('funcionario/anos/', views.get_anos, name='get_anos'),
    path('funcionario/matricula/ucs_matriculadas/<int:id_matricula>/', views.get_ucs_matriculadas, name="get_ucs_matriculadas"),
    path("funcionario/anos_curso/<int:curso_id>/", views.get_anos_curso, name="funcionario_get_anos_curso"),
    path('funcionario/ucs/<int:curso_id>/<int:ano_id>/', views.get_ucs, name='get_ucs'),
    path('funcionario/turnos/<int:uc_id>/', views.get_turnos, name='get_turnos'),
    path('funcionario/matricula/atualizar/<int:id_matricula>/', views.funcionario_atualizar_matricula, name='funcionario_atualizar_matricula'),
    path('funcionario/matricula/remover/<int:id_matricula>/', views.funcionario_delete_matricula, name='funcionario_delete_matricula'),

    path('professor/unidades_curriculares/', views.unidades_curriculares_professor, name='unidades_curriculares_professor'),
    path('funcionario/unidades_curriculares/', views.unidades_curriculares_funcionario, name='unidades_curriculares_funcionario'),
    
    path('funcionario/obter_horarios/', views.obter_horarios_turno, name='obter_horarios_turno'),

    path('funcionarios/alunos/', views.alunos_funcionario, name='alunos_funcionario'),
    path('funcionarios/delete/<int:id_aluno>/', views.aluno_delete, name='aluno_delete'),
    path('funcionarios/editar/<int:id_aluno>/', views.aluno_editar, name='aluno_editar'),

    path('funcionarios/pagamentos/delete/<int:id_pagamento>/', views.funcionario_delete_pagamentos, name='funcionario_delete_pagamentos'),
    path('funcionarios/pagamentos/update/<int:id_pagamento>/', views.funcionario_update_pagamentos, name='funcionario_update_pagamentos'),

    path('aluno/gestao_escola/', views.gestao_escola_aluno, name='gestao_escola_aluno'),
    path('professor/gestao_escola/', views.gestao_escola_professor, name='gestao_escola_professor'),
    path('funcionario/gestao_escola/', views.gestao_escola_funcionario, name='gestao_escola_funcionario'),

]

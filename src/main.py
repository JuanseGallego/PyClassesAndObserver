import observer_practice.canal
import observer_practice.suscriptores

canal = observer_practice.canal.CanalNoticias("Noticias")
suscriptor1 = observer_practice.suscriptores.SuscriptorEmail("Alice")
suscriptor2 = observer_practice.suscriptores.SuscriptorSMS("Bob")

canal.suscribir(suscriptor1)
canal.suscribir(suscriptor2)

canal.publicar("Últimas noticias: Python es el mejor lenguaje de programación.")
print(f"{suscriptor1} ha recibido: {suscriptor1.mensajes}")
print(f"{suscriptor2} ha recibido: {suscriptor2.mensajes}")


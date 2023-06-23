import numpy as np
import matplotlib.pyplot as plt
import os
import networkx as nx
import random
from scipy.integrate import trapz
from scipy.signal import argrelextrema


#Clase de epidemia sis, los parametros del objeto son:
#gamma,beta y N. Luego el numero de susceptibles , de infectados y el tiempo inicial.
class SIS:
    def __init__(self,gamma, beta, N, S,I,t,t_max ):
        self.gamma=gamma
        self.beta=beta
        self.N=N
        self.t=t
        self.S=S
        self.I=I
        #self.R=R
        self.time_list=[t]
        self.S_list = [S]
        self.I_list = [I]
        self.t_max=t_max

    #Función que calcula los rates.
    def rates(self):
        infection_rate = self.beta * self.S * self.I / self.N
        recovery_rate = self.gamma * self.I
        return infection_rate, recovery_rate

    #Metodo para graficar la epidemia, una vez realizada la simulación i y j 
    def Graficar(self):
        # Graficar los resultados
        plt.clf()
        plt.plot(self.time_list, self.S_list, label="Susceptibles")
        plt.plot(self.time_list, self.I_list, label="Infectados")
        #plt.plot(time_list, R_list, label="Recuperados")
        plt.xlabel("Tiempo")
        plt.ylabel("Número de individuos")
        plt.legend()
        # Crear la carpeta donde se va aguardar si no existe
        if not os.path.exists("Imagenes"):
            os.makedirs("Imagenes")
        if not os.path.exists(os.path.join("Imagenes", "SIS")):
            os.makedirs(os.path.join("Imagenes", "SIS"))

        # Guardar la figura en la carpeta "imagenes" dentro de "proyecto"
        filepath = os.path.join("Imagenes", "SIS", "Figura_{0}_{1}.png".format(self.gamma,self.beta))
        plt.savefig(filepath)
        


    #función que simula la epidemia comoleta y devuele los resultados en los vectores
    def Simular(self):
        while (self.I > 0) and self.t<self.t_max:
            # Calcular las tasas de infección y recuperación
            infection_rate, recovery_rate = self.rates()

            # Calcular el tiempo hasta el próximo evento
            total_rate = infection_rate + recovery_rate
            delta_t = -np.log(np.random.random())/total_rate

            # Elegir aleatoriamente el tipo de evento que ocurre
            event = np.random.choice(["infection", "recovery"], p=[infection_rate/total_rate, recovery_rate/total_rate])

            # Actualizar las poblaciones y el tiempo
            if event == "infection":
                self.S -= 1
                self.I += 1
            else:
                self.I -= 1
                #R += 1
                self.S += 1
            self.t += delta_t

            # Almacenar los resultados
            self.time_list.append(self.t)
            self.S_list.append(self.S)
            self.I_list.append(self.I)
            #R_list.append(R)


class SIR:
    def __init__(self,gamma, beta, N, S,I,R,t):
        self.gamma=gamma
        self.beta=beta
        self.N=N
        self.t=t
        self.S=S
        self.I=I
        self.R=R
        self.time_list=[t]        
        self.S_list = [S]
        self.I_list = [I]
        self.R_list=[R]
        


    #Función que calcula los rates.
    def rates(self):
        infection_rate = self.beta * self.S * self.I / self.N
        recovery_rate = self.gamma * self.I
        return infection_rate, recovery_rate

    #Metodo para graficar la epidemia, una vez realizada la simulación i y j 
    def Graficar(self):
        # Graficar los resultados
        plt.clf()
        plt.plot(self.time_list, self.S_list, label="Susceptibles")
        plt.plot(self.time_list, self.I_list, label="Infectados")
        plt.plot(self.time_list, self.R_list, label="Recuperados")
        #plt.plot(time_list, R_list, label="Recuperados")
        plt.xlabel("Tiempo")
        plt.ylabel("Número de individuos")
        plt.legend()
        # Crear la carpeta donde se va aguardar si no existe
        if not os.path.exists("Imagenes"):
            os.makedirs("Imagenes")
        if not os.path.exists(os.path.join("Imagenes", "SIR")):
            os.makedirs(os.path.join("Imagenes", "SIR"))

        # Guardar la figura en la carpeta "imagenes" dentro de "proyecto"
        filepath = os.path.join("Imagenes", "SIR", "Figura_{0}_{1}.png".format(self.gamma,self.beta))
        plt.savefig(filepath)
        
        


    def Simular(self):
            while (self.I > 0):
                # Calcular las tasas de infección y recuperación
                infection_rate, recovery_rate = self.rates()

                # Calcular el tiempo hasta el próximo evento
                total_rate = infection_rate + recovery_rate
                delta_t = -np.log(np.random.random())/total_rate

            # Elegir aleatoriamente el tipo de evento que ocurre
                event = np.random.choice(["infection", "recovery"], p=[infection_rate/total_rate, recovery_rate/total_rate])

            # Actualizar las poblaciones y el tiempo
                if event == "infection":
                    self.S -= 1
                    self.I += 1
                else:
                    self.I -= 1
                    self.R += 1
                    #self.S += 1
                self.t += delta_t

                # Almacenar los resultados
                self.time_list.append(self.t)
                self.S_list.append(self.S)
                self.I_list.append(self.I)
                self.R_list.append(self.R)



class SEIR:
    def __init__(self,gamma,a, beta, N, S,E,I,R,t):
        self.gamma=gamma
        self.beta=beta
        self.a=a
        self.N=N
        self.t=t
        self.S=S
        self.I=I
        self.E=E
        self.R=R
        self.time_list=[t]        
        self.S_list = [S]
        self.E_list = [E]
        self.I_list = [I]
        self.R_list=[R]

    #Metodo para graficar la epidemia, una vez realizada la simulación i y j 
    def Graficar(self):
        # Graficar los resultados
        plt.clf()
        plt.plot(self.time_list, self.S_list, label="Susceptibles")
        plt.plot(self.time_list, self.I_list, label="Infectados")
        plt.plot(self.time_list, self.E_list, label="Expuestos")
        plt.plot(self.time_list, self.R_list, label="Recuperados")
        #plt.plot(time_list, R_list, label="Recuperados")
        plt.xlabel("Tiempo")
        plt.ylabel("Número de individuos")
        plt.legend()
        # Crear la carpeta donde se va aguardar si no existe
        if not os.path.exists("Imagenes"):
            os.makedirs("Imagenes")
        if not os.path.exists(os.path.join("Imagenes", "SEIR")):
            os.makedirs(os.path.join("Imagenes", "SEIR"))

        # Guardar la figura en la carpeta "imagenes" dentro de "proyecto"
        filepath = os.path.join("Imagenes", "SEIR", "Figura_{0}_{1}_{2}.png".format(self.gamma,self.beta,self.a))
        plt.savefig(filepath)
        


    #Función que calcula los rates.
    def rates(self):
        exposition_rate = self.beta * self.S * self.I / self.N
        recovery_rate = self.gamma * self.I
        infection_rate = self.a * self.E
        return exposition_rate, recovery_rate, infection_rate




    def Simular(self):
            while (self.I > 0):
                # Calcular las tasas de infección y recuperación
                exposition_rate, recovery_rate, infection_rate = self.rates()

                # Calcular el tiempo hasta el próximo evento
                total_rate = infection_rate + recovery_rate + exposition_rate
                delta_t = -np.log(np.random.random())/total_rate

            # Elegir aleatoriamente el tipo de evento que ocurre
                event = np.random.choice(["infection", "recovery","exposition"], p=[infection_rate/total_rate, recovery_rate/total_rate,exposition_rate/total_rate])

            # Actualizar las poblaciones y el tiempo
                if event == "infection":
                    self.E -= 1
                    self.I += 1
                elif event == "exposition":
                    self.S -= 1
                    self.E += 1
                else:
                    self.I -= 1
                    self.R += 1
                    #self.S += 1
                self.t += delta_t

                # Almacenar los resultados
                self.time_list.append(self.t)
                self.S_list.append(self.S)
                self.E_list.append(self.E)
                self.I_list.append(self.I)
                self.R_list.append(self.R)


class SIRS:
    def __init__(self,gamma,alfa, beta, N, S,I,R,t,tmax):
        self.gamma=gamma
        self.beta=beta
        self.alfa=alfa
        self.N=N
        self.t=t
        self.tmax=tmax
        self.S=S
        self.I=I        
        self.R=R
        self.time_list=[t]        
        self.S_list = [S]       
        self.I_list = [I]
        self.R_list=[R]

    #Metodo para graficar la epidemia, una vez realizada la simulación i y j 
    def Graficar(self):
        # Graficar los resultados
        plt.clf()
        plt.plot(self.time_list, self.S_list, label="Susceptibles")
        plt.plot(self.time_list, self.I_list, label="Infectados")
        plt.plot(self.time_list, self.R_list, label="Recuperados")
        #plt.plot(time_list, R_list, label="Recuperados")
        plt.xlabel("Tiempo")
        plt.ylabel("Número de individuos")
        plt.legend()
        # Crear la carpeta donde se va aguardar si no existe
        if not os.path.exists("Imagenes"):
            os.makedirs("Imagenes")
        if not os.path.exists(os.path.join("Imagenes", "SIRS")):
            os.makedirs(os.path.join("Imagenes", "SIRS"))

        # Guardar la figura en la carpeta "imagenes" dentro de "proyecto"
        filepath = os.path.join("Imagenes", "SIRS", "Figura_{0}_{1}_{2}.png".format(self.gamma,self.beta,self.alfa))
        plt.savefig(filepath)
        


    #Función que calcula los rates.
    def rates(self):
        infection_rate = self.beta * self.S * self.I / self.N
        recovery_rate = self.gamma * self.I
        susceptition_rate = self.alfa * self.R
        return infection_rate, recovery_rate, susceptition_rate




    def Simular(self):
            while (self.I > 0)and self.t<self.tmax:
                # Calcular las tasas de infección y recuperación
                infection_rate, recovery_rate, susceptition_rate= self.rates()

                # Calcular el tiempo hasta el próximo evento
                total_rate = infection_rate + recovery_rate + susceptition_rate
                delta_t = -np.log(np.random.random())/total_rate

            # Elegir aleatoriamente el tipo de evento que ocurre
                event = np.random.choice(["infection", "recovery","susceptition"], p=[infection_rate/total_rate, recovery_rate/total_rate,susceptition_rate/total_rate])

            # Actualizar las poblaciones y el tiempo
                if event == "infection":
                    self.S -= 1
                    self.I += 1
                elif event == "recovery":
                    self.I -= 1
                    self.R += 1
                else:
                    self.R -= 1
                    self.S += 1
                    #self.S += 1
                self.t += delta_t

                # Almacenar los resultados
                self.time_list.append(self.t)
                self.S_list.append(self.S)
                self.I_list.append(self.I)
                self.R_list.append(self.R)



class MSIR:
    def __init__(self,gamma,delta, beta, N, S,M,I,R,t):
        self.gamma=gamma
        self.beta=beta
        self.delta=delta
        self.N=N
        self.t=t
        self.S=S
        self.I=I
        self.M=M
        self.R=R
        self.time_list=[t]        
        self.S_list = [S]
        self.M_list = [M]
        self.I_list = [I]
        self.R_list=[R]



    def Graficar(self):
        # Graficar los resultados
        plt.clf()
        plt.plot(self.time_list, self.S_list, label="Susceptibles")
        plt.plot(self.time_list, self.I_list, label="Infectados")
        plt.plot(self.time_list, self.M_list, label="Masa con inmunidad pasiva")
        plt.plot(self.time_list, self.R_list, label="Recuperados")
        #plt.plot(time_list, R_list, label="Recuperados")
        plt.xlabel("Tiempo")
        plt.ylabel("Número de individuos")
        plt.legend()
        # Crear la carpeta donde se va aguardar si no existe
        if not os.path.exists("Imagenes"):
            os.makedirs("Imagenes")
        if not os.path.exists(os.path.join("Imagenes", "MSIR")):
            os.makedirs(os.path.join("Imagenes", "MSIR"))

        # Guardar la figura en la carpeta "imagenes" dentro de "proyecto"
        filepath = os.path.join("Imagenes", "MSIR", "Figura_{0}_{1}_{2}.png".format(self.gamma,self.beta,self.delta))
        plt.savefig(filepath)
        


    #Función que calcula los rates.
    def rates(self):
        infection_rate = self.beta * self.S * self.I / self.N
        recovery_rate = self.gamma * self.I
        susception_rate = self.delta * self.M
        return infection_rate, recovery_rate, susception_rate




    def Simular(self):
            while (self.I > 0):
                # Calcular las tasas de infección y recuperación
                infection_rate, recovery_rate, susception_rate = self.rates()

                # Calcular el tiempo hasta el próximo evento
                total_rate = infection_rate + recovery_rate + susception_rate
                delta_t = -np.log(np.random.random())/total_rate

            # Elegir aleatoriamente el tipo de evento que ocurre
                event = np.random.choice(["infection", "recovery","susception"], p=[infection_rate/total_rate, recovery_rate/total_rate, susception_rate/total_rate])

            # Actualizar las poblaciones y el tiempo
                if event == "infection":
                    self.S -= 1
                    self.I += 1
                elif event == "susception":
                    self.M -= 1
                    self.S += 1
                else:
                    self.I -= 1
                    self.R += 1
                    #self.S += 1
                self.t += delta_t

                # Almacenar los resultados
                self.time_list.append(self.t)
                self.S_list.append(self.S)
                self.M_list.append(self.M)
                self.I_list.append(self.I)
                self.R_list.append(self.R)







#Intento 1 de hacer una buena simulación con vacunación, esto es en campo medio, luego copipasteo equisdé
#
#Tendremos las siguientes reacciones
# 1      V+I_v-gammav1>2I_v           
#  2     V+I-gammav2>I_v+I     
#   3    S+I-gammas1>2I    
#  4     S+I_v-gammas2>I+I_v   
# 5      Sn+I-gammasn1>2I     
#  6     Sn+I_v-gammasn2>I+I_v
#   7    S-alfa>V       
#  8     S-beta>Sn       
#   9    S-sigma>S(puede ser cero)      
#    10  I-nu>R      
#    11  I_v-nuv>R_v
#        Usare rate 1 2 3 y así en este orden.
#
#       V=vacunados            S=que se quieren vacunar            Sn=que no quieren       
#       I=infectados        I_v=Infectados vacunados        R=recuperados o muertos
#       gammas son de infección
#       alfa es vacunación constante
#       beta y sigma será o no, cosas sociales
#       nu recuperaciones


class Prototipo1:

    #de momento se supone se empieza sin vacunados
    def __init__(self,gammav1,gammav2,gammas1,gammas2,gammasn1,gammasn2,alfa, beta,sigma,nu,nuv, N, S,Sn,I,R,t):
        self.gammav1=gammav1
        self.gammav2=gammav2
        self.gammas1=gammas1
        self.gammas2=gammas2
        self.gammasn1=gammasn1
        self.gammasn2=gammasn2
        self.alfa=alfa
        self.sigma=sigma
        self.nu=nu
        self.nuv=nuv
        self.beta=beta
        self.N=N
        self.t=t
        self.S=S
        self.Sn=Sn
        V=0
        self.V=V
        self.I=I
        I_v=0
        self.I_v=I_v
        self.R=R
        self.time_list=[t]        
        self.S_list = [S]
        self.I_list = [I]
        self.Sn_list = [Sn]
        self.V_list = [V]
        self.I_v_list = [I_v]
        self.R_list=[R]


    #Tendremos las siguientes reacciones
    # 1      V+I_v-gammav1>2I_v           
    #  2     V+I-gammav2>I_v+I     
    #   3    S+I-gammas1>2I    
    #  4     S+I_v-gammas2>I+I_v   
    # 5      Sn+I-gammasn1>2I     
    #  6     Sn+I_v-gammasn2>I+I_v
    #   7    S-alfa>V       
    #  8     S-beta>Sn       
    #   9    S-sigma>S(puede ser cero)      
    #    10  I-nu>R      
    #    11  I_v-nuv>R_v
    #        Usare rate 1 2 3 y así en este orden.
    def rates(self):
        r1=self.gammav1*self.V*self.I_v/self.N
        r2=self.gammav2*self.V*self.I/self.N
        r3=self.gammas1*self.S*self.I/self.N
        r4=self.gammas2*self.S*self.I_v/self.N
        r5=self.gammasn1*self.Sn*self.I/self.N
        r6=self.gammasn2*self.Sn*self.I_v/self.N
        if self.S!=0 and self.Sn!=0 :
            r7=self.alfa*self.N
        else:
            r7=0
        r10=self.nu*self.I
        r11=self.nuv*self.I_v   


        
        r8=self.beta*self.S
        r9=self.sigma*self.Sn     
       
        return r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11



    #Tendremos las siguientes reacciones
    # 1      V+I_v-gammav1>2I_v           
    #  2     V+I-gammav2>I_v+I     
    #   3    S+I-gammas1>2I    
    #  4     S+I_v-gammas2>I+I_v   
    # 5      Sn+I-gammasn1>2I     
    #  6     Sn+I_v-gammasn2>I+I_v
    #   7    S-alfa>V       
    #  8     S-beta>Sn       
    #   9    S-sigma>S(puede ser cero)      
    #    10  I-nu>R      
    #    11  I_v-nuv>R_v
    #        Usare rate 1 2 3 y así en este orden.
    def Simular(self):
            while (self.I > 0):
                # Calcular las tasas de infección y recuperación
                r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11 = self.rates()

                # Calcular el tiempo hasta el próximo evento
                tr = r1+r2+r3+r4+r5+r6+r7+r10+r11
                tr2 = r8+r9
                delta_t = -np.log(np.random.random())/tr

            # Elegir aleatoriamente el tipo de evento que ocurre
                event = np.random.choice(["r1","r2","r3","r4","r5","r6","r7","r10","r11"], p=[r1/tr,r2/tr,r3/tr,r4/tr,r5/tr,r6/tr,r7/tr,r10/tr,r11/tr])


                # Elegir aleatoriamente el tipo de evento que ocurre
                if tr2!=0:
                    event2 = np.random.choice(["r8","r9"], p=[r8/tr2,r9/tr2])

            # Actualizar las poblaciones y el tiempo
                if event == "r1":
                    self.V -= 1
                    self.I_v += 1
                elif event == "r2":
                    self.V -= 1
                    self.I_v += 1
                elif event == "r3":
                    self.S -= 1
                    self.I += 1
                elif event == "r4":
                    self.S -= 1
                    self.I += 1
                elif event == "r5":
                    self.Sn -= 1
                    self.I += 1
                elif event == "r6":
                    self.Sn -= 1
                    self.I += 1
                elif event == "r7":
                    self.S -= 1
                    self.V += 1
                
                elif event == "r10":
                    self.I -= 1
                    self.R += 1
                else:
                    self.I_v -= 1
                    self.R += 1    
                if self.S!=0 and self.Sn!=0 :
                    if event2 == "r8":
                        self.S -= 1
                        self.Sn += 1
                    else:
                        self.Sn -= 1
                        self.S += 1               
                self.t += delta_t

                # Almacenar los resultados
                self.time_list.append(self.t)
                self.S_list.append(self.S)
                self.Sn_list.append(self.Sn)
                self.V_list.append(self.V)
                self.I_list.append(self.I)
                self.I_v_list.append(self.I_v)
                self.R_list.append(self.R)






    def Graficar(self):
        # Graficar los resultados
        plt.clf()
        #sumo las listas 
        Stlist = [x + y for x, y in zip(self.S_list,self.Sn_list)]
        ItList = [x + y for x, y in zip(self.I_list,self.I_v_list)]
        plt.plot(self.time_list, Stlist , label="Susceptibles")
        plt.plot(self.time_list, self.V_list, label="Vacunados sanos")
        plt.plot(self.time_list, ItList, label="Infectados")        
        plt.plot(self.time_list, self.R_list, label="Recuperados")
        #plt.plot(time_list, R_list, label="Recuperados")
        plt.xlabel("Tiempo")
        plt.ylabel("Número de individuos")
        #texto="Figura_{0}_{1}_\n{2}_{3}_{4}\n_{5}_{6}_{7}\n_{8}_{9}_\n{10}.png".format(self.gammav1,self.gammav2,self.gammas1,self.gammas2,self.gammasn1,self.gammasn2,self.alfa,self.beta,self.sigma,self.nu,self.nuv)
        #plt.text(4.5, 9, texto, ha='right',va='top')
        plt.legend()
        # Crear la carpeta donde se va aguardar si no existe
        if not os.path.exists("Imagenes"):
            os.makedirs("Imagenes")
        if not os.path.exists(os.path.join("Imagenes", "PROTOTIPO1")):
            os.makedirs(os.path.join("Imagenes", "PROTOTIPO1"))

        # Guardar la figura en la carpeta "imagenes" dentro de "proyecto"
        filepath = os.path.join("Imagenes", "PROTOTIPO1", "Ejemplo")
        plt.savefig(filepath)
        





class Prototipo1mv:

    #de momento se supone se empieza sin vacunados
    def __init__(self,gammav1,gammav2,gammas1,gammas2,gammasn1,gammasn2,alfa, beta,sigma,nu,nuv,vitality, N, S,Sn,I,R,t,tiempovacuna,tmax):
        self.gammav1=gammav1
        self.gammav2=gammav2
        self.gammas1=gammas1
        self.gammas2=gammas2
        self.gammasn1=gammasn1
        self.gammasn2=gammasn2
        self.alfa=alfa
        self.sigma=sigma
        self.nu=nu
        self.nuv=nuv
        self.beta=beta
        self.vitality=vitality
        self.tmax=tmax
        self.tiempovacuna=tiempovacuna
        self.N=N
        self.t=t
        self.S=S
        self.Sn=Sn
        V=0
        self.V=V
        self.I=I
        I_v=0
        self.I_v=I_v
        self.R=R
        self.time_list=[t]        
        self.S_list = [S]
        self.I_list = [I]
        self.Sn_list = [Sn]
        self.V_list = [V]
        self.I_v_list = [I_v]
        self.R_list=[R]


    #Tendremos las siguientes reacciones
    # 1      V+I_v-gammav1>2I_v           
    #  2     V+I-gammav2>I_v+I     
    #   3    S+I-gammas1>2I    
    #  4     S+I_v-gammas2>I+I_v   
    # 5      Sn+I-gammasn1>2I     
    #  6     Sn+I_v-gammasn2>I+I_v
    #   7    S-alfa>V       
    #  8     S-beta>Sn       
    #   9    S-sigma>S(puede ser cero)      
    #    10  I-nu>R      
    #    11  I_v-nuv>R_v
    #        Usare rate 1 2 3 y así en este orden.
    def rates(self):
        r1=self.gammav1*self.V*self.I_v/self.N
        r2=self.gammav2*self.V*self.I/self.N
        r3=self.gammas1*self.S*self.I/self.N
        r4=self.gammas2*self.S*self.I_v/self.N
        r5=self.gammasn1*self.Sn*self.I/self.N
        r6=self.gammasn2*self.Sn*self.I_v/self.N
        if self.S!=0 and self.Sn!=0 :
            r7=self.alfa*self.N
        else:
            r7=0
        r10=self.nu*self.I
        r11=self.nuv*self.I_v   


        
        r8=self.beta*self.S
        r9=self.sigma*self.Sn     
       
        return r1,r2,r3,r4,r5,r6,r8,r9,r10,r11



    #Tendremos las siguientes reacciones
    # 1      V+I_v-gammav1>2I_v           
    #  2     V+I-gammav2>I_v+I     
    #   3    S+I-gammas1>2I    
    #  4     S+I_v-gammas2>I+I_v   
    # 5      Sn+I-gammasn1>2I     
    #  6     Sn+I_v-gammasn2>I+I_v
    #   7    S-alfa>V       
    #  8     S-beta>Sn       
    #   9    S-sigma>S(puede ser cero)      
    #    10  I-nu>R      
    #    11  I_v-nuv>R_v
    #        Usare rate 1 2 3 y así en este orden.
    def Simular(self):
            while (self.I > 0) and self.t<self.tmax:
                # Calcular las tasas de infección y recuperación
                r1,r2,r3,r4,r5,r6,r8,r9,r10,r11 = self.rates()

                # Calcular el tiempo hasta el próximo evento
                tr = r1+r2+r3+r4+r5+r6+r10+r11
                tr2 = r8+r9
                delta_t = -np.log(np.random.random())/tr

            # Elegir aleatoriamente el tipo de evento que ocurre
                event = np.random.choice(["r1","r2","r3","r4","r5","r6","r10","r11"], p=[r1/tr,r2/tr,r3/tr,r4/tr,r5/tr,r6/tr,r10/tr,r11/tr])


                # Elegir aleatoriamente el tipo de evento que ocurre
                if tr2!=0:
                    event2 = np.random.choice(["r8","r9"], p=[r8/tr2,r9/tr2])

            # Actualizar las poblaciones y el tiempo
                if event == "r1":
                    self.V -= 1
                    self.I_v += 1
                elif event == "r2":
                    self.V -= 1
                    self.I_v += 1
                elif event == "r3":
                    self.S -= 1
                    self.I += 1
                elif event == "r4":
                    self.S -= 1
                    self.I += 1
                elif event == "r5":
                    self.Sn -= 1
                    self.I += 1
                elif event == "r6":
                    self.Sn -= 1
                    self.I += 1
                
                elif event == "r10":
                    self.I -= 1
                    self.R += 1
                else:
                    self.I_v -= 1
                    self.R += 1    
                if self.S!=0 and self.Sn!=0 :
                    if event2 == "r8":
                        self.S -= 1
                        self.Sn += 1
                    else:
                        self.Sn -= 1
                        self.S += 1               
                self.t += delta_t


                muerte=np.random.choice(['muere','nada'],p=[self.vitality,1-self.vitality])
                vacunación=np.random.choice(['vacuna','nada'],p=[self.alfa*self.I/self.N,1-self.alfa*self.I/self.N])
                if muerte=='muere' and self.R!=0:
                    grupo=np.random.choice(['s','sn'],p=[self.S/(self.S+self.Sn),self.Sn/(self.S+self.Sn)])
                    if grupo=='s':
                        self.R-=1
                        self.S+=1
                    else :
                        self.R-=1
                        self.Sn+=1
                if vacunación=='vacuna'and self.S!=0:
                    self.S-=1
                    self.V+=1
                # Almacenar los resultados
                self.time_list.append(self.t)
                self.S_list.append(self.S)
                self.Sn_list.append(self.Sn)
                self.V_list.append(self.V)
                self.I_list.append(self.I)
                self.I_v_list.append(self.I_v)
                self.R_list.append(self.R)






    def Graficar1(self):
        # Graficar los resultados
        plt.clf()
        #sumo las listas 
        Stlist = [x + y for x, y in zip(self.S_list,self.Sn_list)]
        ItList = [x + y for x, y in zip(self.I_list,self.I_v_list)]
        plt.plot(self.time_list, Stlist , label="Susceptibles")
        plt.plot(self.time_list, self.V_list, label="Vacunados sanos")
        plt.plot(self.time_list, ItList, label="Infectados")        
        plt.plot(self.time_list, self.R_list, label="Recuperados")
        #plt.plot(time_list, R_list, label="Recuperados")
        plt.xlabel("Tiempo")
        plt.ylabel("Número de individuos")
        #texto="Figura_{0}_{1}_\n{2}_{3}_{4}\n_{5}_{6}_{7}\n_{8}_{9}_\n{10}.png".format(self.gammav1,self.gammav2,self.gammas1,self.gammas2,self.gammasn1,self.gammasn2,self.alfa,self.beta,self.sigma,self.nu,self.nuv)
        #plt.text(4.5, 9, texto, ha='right',va='top')
        plt.legend()
        # Crear la carpeta donde se va aguardar si no existe
        if not os.path.exists("Imagenes"):
            os.makedirs("Imagenes")
        if not os.path.exists(os.path.join("Imagenes", "PROTOTIPO1mv")):
            os.makedirs(os.path.join("Imagenes", "PROTOTIPO1mv"))
        if not os.path.exists(os.path.join("Imagenes", "PROTOTIPO1mv", "{0}_{1}_{2}_{3}_{4}".format(self.alfa,self.beta,self.sigma,self.tiempovacuna,self.vitality))):
            os.makedirs(os.path.join("Imagenes", "PROTOTIPO1mv", "{0}_{1}_{2}_{3}_{4}".format(self.alfa,self.beta,self.sigma,self.tiempovacuna,self.vitality)))

        # Guardar la figura en la carpeta "imagenes" dentro de "proyecto"
        filepath = os.path.join("Imagenes", "PROTOTIPO1mv", "{0}_{1}_{2}_{3}_{4}".format(self.alfa,self.beta,self.sigma,self.tiempovacuna,self.vitality),"resumen.png")
        plt.savefig(filepath)
        #print('Simulacion1 realizada.')
        


    def Graficar2(self):
        # Graficar los resultados
        plt.clf()
        #sumo las listas 
        
        plt.plot(self.time_list, self.Sn_list , label="Susceptibles antivacunas")
        plt.plot(self.time_list, self.S_list , label="Susceptibles provacunas")
        plt.plot(self.time_list, self.V_list, label="Vacunados sanos")
        plt.plot(self.time_list, self.I_list, label="Infectados no vacunados")        
        plt.plot(self.time_list, self.I_v_list, label="Infectados vacunados") 
        plt.plot(self.time_list, self.R_list, label="Recuperados")
        #plt.plot(time_list, R_list, label="Recuperados")
        plt.xlabel("Tiempo")
        plt.ylabel("Número de individuos")
        #texto="Figura_{0}_{1}_\n{2}_{3}_{4}\n_{5}_{6}_{7}\n_{8}_{9}_\n{10}.png".format(self.gammav1,self.gammav2,self.gammas1,self.gammas2,self.gammasn1,self.gammasn2,self.alfa,self.beta,self.sigma,self.nu,self.nuv)
        #plt.text(4.5, 9, texto, ha='right',va='top')
        plt.legend()
        # Crear la carpeta donde se va aguardar si no existe
        if not os.path.exists("Imagenes"):
            os.makedirs("Imagenes")
        if not os.path.exists(os.path.join("Imagenes", "PROTOTIPO1mv")):
            os.makedirs(os.path.join("Imagenes", "PROTOTIPO1mv"))
        if not os.path.exists(os.path.join("Imagenes", "PROTOTIPO1mv", "{0}_{1}_{2}_{3}_{4}".format(self.alfa,self.beta,self.sigma,self.tiempovacuna,self.vitality))):
            os.makedirs(os.path.join("Imagenes", "PROTOTIPO1mv", "{0}_{1}_{2}_{3}_{4}".format(self.alfa,self.beta,self.sigma,self.tiempovacuna,self.vitality)))

        # Guardar la figura en la carpeta "imagenes" dentro de "proyecto"
        filepath = os.path.join("Imagenes", "PROTOTIPO1mv", "{0}_{1}_{2}_{3}_{4}".format(self.alfa,self.beta,self.sigma,self.tiempovacuna,self.vitality),"todos.png")
        plt.savefig(filepath)
        #print('Simulacion2 realizada.')
        
        
    def Fichero(self):
        if not os.path.exists("Imagenes"):
            os.makedirs("Imagenes")
        if not os.path.exists(os.path.join("Imagenes", "PROTOTIPO1mv")):
            os.makedirs(os.path.join("Imagenes", "PROTOTIPO1mv"))
        if not os.path.exists(os.path.join("Imagenes", "PROTOTIPO1mv", "{0}_{1}_{2}_{3}_{4}".format(self.alfa,self.beta,self.sigma,self.tiempovacuna,self.vitality))):
            os.makedirs(os.path.join("Imagenes", "PROTOTIPO1mv", "{0}_{1}_{2}_{3}_{4}".format(self.alfa,self.beta,self.sigma,self.tiempovacuna,self.vitality)))

        # Nombre del archivo
        nombre_archivo = os.path.join("Imagenes", "PROTOTIPO1mv", "{0}_{1}_{2}_{3}_{4}".format(self.alfa,self.beta,self.sigma,self.tiempovacuna,self.vitality), 'datos.txt')

        # Obtiene la longitud máxima de las listas
        longitud_maxima = max(len(self.time_list), len(self.S_list), len(self.Sn_list), len(self.V_list), len(self.I_list),len(self.I_v_list), len(self.R_list))

        # Abre el archivo en modo escritura
        with open(nombre_archivo, 'w') as archivo:
            # Escribe los elementos de cada lista en columnas correspondientes
            for i in range(longitud_maxima):
                if i < len(self.time_list):
                    archivo.write(str(self.time_list[i]) + '\t')
                else:
                    archivo.write('\t')
                
                if i < len(self.S_list):
                    archivo.write(str(self.S_list[i]) + '\t')
                else:
                    archivo.write('\t')
                
                if i < len(self.Sn_list):
                    archivo.write(str(self.Sn_list[i]) + '\t')
                else:
                    archivo.write('\t')
                
                if i < len(self.V_list):
                    archivo.write(str(self.V_list[i]) + '\t')
                else:
                    archivo.write('\t')
                
                if i < len(self.I_list):
                    archivo.write(str(self.I_list[i]) + '\t')
                else:
                    archivo.write('\t')
                
                if i < len(self.I_v_list):
                    archivo.write(str(self.I_v_list[i]) + '\t')
                else:
                    archivo.write('\t')
                
                if i < len(self.V_list):
                    archivo.write(str(self.R_list[i]) + '\t')
                else:
                    archivo.write('\t')
                archivo.write('\n')
                










#PROTOTIPO2, AHORA INTENTO METER TEORÍA DE REDES
#sOLO CAMBIA COMO SE CALCULAN LOS RATES Y COMO CAMBIAN LOS NUMEROS DE GRUPOS


class Prototipo2:

    #de momento se supone se empieza sin vacunados
    def __init__(self,gammav1,gammav2,gammas1,gammas2,gammasn1,gammasn2,alfa, beta,sigma,nu,nuv, N,V, S,Sn,I,R,t,tvacuna):
        self.gammav1=gammav1
        self.gammav2=gammav2
        self.gammas1=gammas1
        self.gammas2=gammas2
        self.gammasn1=gammasn1
        self.gammasn2=gammasn2
        self.alfa=alfa
        self.sigma=sigma
        self.nu=nu
        self.nuv=nuv
        self.beta=beta
        self.N=N
        self.t=t
        self.S=S
        self.Sn=Sn
        
        self.V=V
        self.I=I
        I_v=0
        self.I_v=I_v
        self.R=R
        self.time_list=[t]        
        self.S_list = [S]
        self.I_list = [I]
        self.Sn_list = [Sn]
        self.V_list = [V]
        self.I_v_list = [I_v]
        self.R_list=[R]
        self.tiempovacuna=tvacuna
        #REDES A USAR 

        # Parámetros DE LAS REDES, SUPONGO QUE NO NOS INTERESA VER COMO CAMBIAN EL RESULTADO
        # ASI QUE PONEMOS UNOS Y YA ESTA
        k = 14  # Grado promedio de los nodos
        p = 0.6  # Probabilidad de "rewiring"
        self.graph1 = nx.watts_strogatz_graph(N, k, p)
        m = 6  # Número de conexiones iniciales para cada nodo nuevo
        self.graph2 = nx.barabasi_albert_graph(N, m)
        #INICIALIZO LOS ESTADOS AL AZAR EN LA RED CON CONEXIONES YA CREADAS
        estados = ['V'] * V + ['S'] * S + ['Sn'] * Sn + ['I'] * I + ['I_v'] * I_v +['R'] * R
        random.shuffle(estados)


        for i, nodo in enumerate(self.graph1.nodes()):
            estado = estados[i]
            self.graph1.nodes[nodo]['state'] = estado
            self.graph2.nodes[nodo]['state'] = estado


        #Listas de estados y vectores de rates de infección
        self.Snodos=[]
        self.Snnodos=[]
        self.Vnodos=[]
        self.Inodos=[]
        self.I_vnodos=[]
        self.Rnodos=[]
        #RATES, QUE VAN DE UN GRUPO A OTRO, ASÍ SE ELEGIRÁ AL QUE MAS RATE TENGA COMO INFECTADO
        self.SRATESI=[]
        self.SRATESI_v=[]
        self.VRATESI=[]
        self.SnRATESI=[]
        self.VRATESI_v=[]
        self.SnRATESI_v=[]
        self.SRATESSn=[]
        self.SnRATESS=[]
        #Inicializo todas las listas con los nodos de cada lista
        for nodo in self.graph1.nodes():
            if self.graph1.nodes[nodo]['state'] == 'S':
                self.Snodos.append(nodo)
            elif self.graph1.nodes[nodo]['state'] == 'Sn':
                self.Snnodos.append(nodo)
            elif self.graph1.nodes[nodo]['state'] == 'V':
                self.Vnodos.append(nodo)
            elif self.graph1.nodes[nodo]['state'] == 'R':
                self.Rnodos.append(nodo)
            elif self.graph1.nodes[nodo]['state'] == 'I':
                self.Inodos.append(nodo)
            elif self.graph1.nodes[nodo]['state'] == 'I_v':
                self.I_vnodos.append(nodo)



    #Tendremos las siguientes reacciones
    # 1      V+I_v-gammav1>2I_v           
    #  2     V+I-gammav2>I_v+I     
    #   3    S+I-gammas1>2I    
    #  4     S+I_v-gammas2>I+I_v   
    # 5      Sn+I-gammasn1>2I     
    #  6     Sn+I_v-gammasn2>I+I_v
    #   7    S-alfa>V       
    #  8     S-beta>Sn       
    #   9    S-sigma>S(puede ser cero)      
    #    10  I-nu>R      
    #    11  I_v-nuv>R_v
    #        Usare rate 1 2 3 y así en este orden.
    #CON TEORÍA DE REDES
    def rates1(self):
        #parte de los infectados
        r1=r2=r3=r4=r5=r6=r7=r10=r11=0
        self.SRATESI=[]
        self.SRATESI_v=[]
        self.VRATESI=[]
        self.SnRATESI=[]
        self.VRATESI_v=[]
        self.SnRATESI_v=[]
        
        
        


        for nodo in self.Snodos:
            vecinos=list(self.graph1.neighbors(nodo))
            SRATESI=SRATESI_v=0
            for vecino in vecinos:
                if vecino in self.Inodos:
                    SRATESI+=self.gammas1                    
                elif vecino in self.I_vnodos:
                    SRATESI_v+=self.gammas2
            self.SRATESI.append(SRATESI)
            self.SRATESI_v.append(SRATESI_v)
            r3+=SRATESI
            r4+=SRATESI_v


        for nodo in self.Vnodos:    
            vecinos=list(self.graph1.neighbors(nodo))           
            VRATESI=VRATESI_v=0
            for vecino in vecinos:
                if vecino in self.Inodos:
                    VRATESI+=self.gammav2                    
                elif vecino in self.I_vnodos:
                    VRATESI_v+=self.gammav1
            self.VRATESI.append(VRATESI)
            self.VRATESI_v.append(VRATESI_v)
            r2+=VRATESI
            r1+=VRATESI_v


        for nodo in self.Snnodos:            
            vecinos=list(self.graph1.neighbors(nodo))
            SnRATESI=SnRATESI_v=0
            for vecino in vecinos:
                if vecino in self.Inodos:
                    SnRATESI+=self.gammasn1                    
                elif vecino in self.I_vnodos:
                    SnRATESI_v+=self.gammasn2
            self.SnRATESI.append(SnRATESI)
            self.SnRATESI_v.append(SnRATESI_v)
            r5+=SnRATESI
            r6+=SnRATESI_v



        
        if self.S!=0 and self.Sn!=0 and self.t>self.tiempovacuna :
            r7=self.alfa*self.N
        else:
            r7=0
        r10=self.nu*self.I
        r11=self.nuv*self.I_v   
        return r1,r2,r3,r4,r5,r6,r7,r10,r11

    #DINAMICA SOCIAL
    def rates2(self):
        r8=r9=0
        self.SRATESSn=[]
        self.SnRATESS=[]
        for nodo in self.Snodos:            
            vecinos=list(self.graph2.neighbors(nodo))
            SRATESSn=0
            for vecino in vecinos:
                if vecino in self.Snnodos:
                    SRATESSn+=self.beta      
            self.SRATESSn.append(SRATESSn)            
            r8+=SRATESSn

            
                
        for nodo in self.Snnodos:     
            vecinos=list(self.graph2.neighbors(nodo))
            SnRATESS=0
            for vecino in vecinos:
                if vecino in self.Snodos:
                    SnRATESS+=self.sigma    
            self.SnRATESS.append(SnRATESS)            
            r9+=SnRATESS
       
        return r8,r9



    #Tendremos las siguientes reacciones
    # 1      V+I_v-gammav1>2I_v           
    #  2     V+I-gammav2>I_v+I     
    #   3    S+I-gammas1>2I    
    #  4     S+I_v-gammas2>I+I_v   
    # 5      Sn+I-gammasn1>2I     
    #  6     Sn+I_v-gammasn2>I+I_v
    #   7    S-alfa>V       
    #  8     S-beta>Sn       
    #   9    S-sigma>S(puede ser cero)      
    #    10  I-nu>R      
    #    11  I_v-nuv>R_v
    #        Usare rate 1 2 3 y así en este orden.
        #CON TEORÍA DE REDES
    def Simular(self):
            while (self.R!=self.N):
                # Calcular las tasas de infección y recuperación
                if self.Sn==0 :
                    #hola
                    #hola
                    a=2
                r1,r2,r3,r4,r5,r6,r7,r10,r11 = self.rates1()

                # Calcular el tiempo hasta el próximo evento
                tr = r1+r2+r3+r4+r5+r6+r7+r10+r11
                if tr==0:
                    break
                
                
                delta_t = -np.log(np.random.random())/tr

            # Elegir aleatoriamente el tipo de evento que ocurre
                event = np.random.choice(["r1","r2","r3","r4","r5","r6","r7","r10","r11"], p=[r1/tr,r2/tr,r3/tr,r4/tr,r5/tr,r6/tr,r7/tr,r10/tr,r11/tr])


                

            # Actualizar las poblaciones y el tiempo
                if event == "r1":
                    self.V -= 1
                    self.I_v += 1
                    eleccion=self.Vnodos[self.VRATESI_v.index(max(self.VRATESI_v))]                    
                    self.Vnodos.remove(eleccion)
                    self.I_vnodos.append(eleccion)


                elif event == "r2":
                    self.V -= 1
                    self.I_v += 1
                    eleccion=self.Vnodos[self.VRATESI.index(max(self.VRATESI))]                    
                    self.Vnodos.remove(eleccion)
                    self.I_vnodos.append(eleccion)



                elif event == "r3":
                    self.S -= 1
                    self.I += 1
                    eleccion=self.Snodos[self.SRATESI.index(max(self.SRATESI))]                   
                    self.Snodos.remove(eleccion)
                    self.Inodos.append(eleccion)


                elif event == "r4":
                    self.S -= 1
                    self.I += 1       
                    eleccion=self.Snodos[self.SRATESI_v.index(max(self.SRATESI_v))]                     
                    self.Snodos.remove(eleccion)
                    self.Inodos.append(eleccion)


                elif event == "r5":
                    self.Sn -= 1
                    self.I += 1      
                    eleccion=self.Snnodos[self.SnRATESI.index(max(self.SnRATESI))]                    
                    self.Snnodos.remove(eleccion)
                    self.Inodos.append(eleccion)



                elif event == "r6":
                    self.Sn -= 1
                    self.I += 1    
                    eleccion=self.Snnodos[self.SnRATESI_v.index(max(self.SnRATESI_v))]  
                    self.Snnodos.remove(eleccion)
                    self.Inodos.append(eleccion)



                elif event == "r7":
                    self.S -= 1
                    self.V += 1
                    eleccion=random.choice(self.Snodos)                    
                    self.Snodos.remove(eleccion)
                    self.Vnodos.append(eleccion)



                
                elif event == "r10":
                    self.I -= 1
                    self.R += 1
                    eleccion=random.choice(self.Inodos)                    
                    self.Inodos.remove(eleccion)
                    self.Rnodos.append(eleccion)


                else:
                    self.I_v -= 1
                    self.R += 1    
                    eleccion=random.choice(self.I_vnodos)                    
                    self.I_vnodos.remove(eleccion)
                    self.Rnodos.append(eleccion)

                r8,r9=self.rates2()
                tr2 = r8+r9
                # Elegir aleatoriamente el tipo de evento que ocurre
                if tr2!=0:
                    event2 = np.random.choice(["r8","r9"], p=[r8/tr2,r9/tr2])
              
                    if event2 == "r8" and self.S!=0:
                        self.S -= 1
                        self.Sn += 1
                        indice=self.SRATESSn.index(max(self.SRATESSn))
                        eleccion=self.Snodos[indice]                        
                        self.Snodos.remove(eleccion)
                        self.Snnodos.append(eleccion)

                    elif self.Sn!=0:
                        self.Sn -= 1
                        self.S += 1    
                        indice=self.SnRATESS.index(max(self.SnRATESS))    
                        eleccion=self.Snnodos[indice]                   
                        self.Snnodos.remove(eleccion)
                        self.Snodos.append(eleccion)


                self.t += delta_t
                #print(self.t)

                # Almacenar los resultados
                self.time_list.append(self.t)
                self.S_list.append(self.S)
                self.Sn_list.append(self.Sn)
                self.V_list.append(self.V)
                self.I_list.append(self.I)
                self.I_v_list.append(self.I_v)
                self.R_list.append(self.R)






    def Graficar1(self):
        # Graficar los resultados
        plt.clf()
        #sumo las listas 
        Stlist = [x + y for x, y in zip(self.S_list,self.Sn_list)]
        ItList = [x + y for x, y in zip(self.I_list,self.I_v_list)]
        plt.plot(self.time_list, Stlist , label="Susceptibles")
        plt.plot(self.time_list, self.V_list, label="Vacunados sanos")
        plt.plot(self.time_list, ItList, label="Infectados")        
        plt.plot(self.time_list, self.R_list, label="Recuperados")
        #plt.plot(time_list, R_list, label="Recuperados")
        plt.xlabel("Tiempo")
        plt.ylabel("Número de individuos")
        #texto="Figura_{0}_{1}_\n{2}_{3}_{4}\n_{5}_{6}_{7}\n_{8}_{9}_\n{10}.png".format(self.gammav1,self.gammav2,self.gammas1,self.gammas2,self.gammasn1,self.gammasn2,self.alfa,self.beta,self.sigma,self.nu,self.nuv)
        #plt.text(4.5, 9, texto, ha='right',va='top')
        plt.legend()
        # Crear la carpeta donde se va aguardar si no existe
        if not os.path.exists("Imagenes"):
            os.makedirs("Imagenes")
        if not os.path.exists(os.path.join("Imagenes", "PROTOTIPO2")):
            os.makedirs(os.path.join("Imagenes", "PROTOTIPO2"))

        # Guardar la figura en la carpeta "imagenes" dentro de "proyecto"
        filepath = os.path.join("Imagenes", "PROTOTIPO2", "Resumen_{0}_{1}_{2}_{3}..png".format(self.alfa,self.beta,self.sigma,self.tiempovacuna))
        plt.savefig(filepath)
        #print('Simulacion1 realizada.')
        


    def Graficar2(self):
        # Graficar los resultados
        plt.clf()
        #sumo las listas 
        
        plt.plot(self.time_list, self.Sn_list , label="Susceptibles antivacunas")
        plt.plot(self.time_list, self.S_list , label="Susceptibles provacunas")
        plt.plot(self.time_list, self.V_list, label="Vacunados sanos")
        plt.plot(self.time_list, self.I_list, label="Infectados no vacunados")        
        plt.plot(self.time_list, self.I_v_list, label="Infectados vacunados") 
        plt.plot(self.time_list, self.R_list, label="Recuperados")
        #plt.plot(time_list, R_list, label="Recuperados")
        plt.xlabel("Tiempo")
        plt.ylabel("Número de individuos")
        #texto="Figura_{0}_{1}_\n{2}_{3}_{4}\n_{5}_{6}_{7}\n_{8}_{9}_\n{10}.png".format(self.gammav1,self.gammav2,self.gammas1,self.gammas2,self.gammasn1,self.gammasn2,self.alfa,self.beta,self.sigma,self.nu,self.nuv)
        #plt.text(4.5, 9, texto, ha='right',va='top')
        plt.legend()
        # Crear la carpeta donde se va aguardar si no existe
        if not os.path.exists("Imagenes"):
            os.makedirs("Imagenes")
        if not os.path.exists(os.path.join("Imagenes", "PROTOTIPO2")):
            os.makedirs(os.path.join("Imagenes", "PROTOTIPO2"))

        # Guardar la figura en la carpeta "imagenes" dentro de "proyecto"
        filepath = os.path.join("Imagenes", "PROTOTIPO2", "Todos_{0}_{1}_{2}_{3}.png".format(self.alfa,self.beta,self.sigma,self.tiempovacuna))
        plt.savefig(filepath)
        #print('Simulacion2 realizada.')
        



#PROTOTIPO3, AHORA INTENTO optimizar TEORÍA DE REDES

class Prototipo3:

    #de momento se supone se empieza sin vacunados
    def __init__(self,gammav1,gammav2,gammas1,gammas2,gammasn1,gammasn2,alfa, beta,sigma,nu,nuv, N,V, S,Sn,I,R,t,tvacuna):
        self.gammav1=gammav1
        self.gammav2=gammav2
        self.gammas1=gammas1
        self.gammas2=gammas2
        self.gammasn1=gammasn1
        self.gammasn2=gammasn2
        self.alfa=alfa
        self.sigma=sigma
        self.nu=nu
        self.nuv=nuv
        self.beta=beta
        #VARIABLES QUE USAREMOS PARA GRAFICAR LOS RESULTADPS
        self.N=N
        self.t=t
        self.S=S
        self.Sn=Sn
        
        self.V=V
        self.I=I
        I_v=0
        self.I_v=I_v
        self.R=R
        self.time_list=[t]        
        self.S_list = [S]
        self.I_list = [I]
        self.Sn_list = [Sn]
        self.V_list = [V]
        self.I_v_list = [I_v]
        self.R_list=[R]
        self.tiempovacuna=tvacuna
        self.r1=self.r2=self.r3=self.r4=self.r5=self.r6=self.r7=self.r8=self.r9=self.r10=self.r11=0
        #REDES A USAR 

        # Parámetros DE LAS REDES, SUPONGO QUE NO NOS INTERESA VER COMO CAMBIAN EL RESULTADO
        # ASI QUE PONEMOS UNOS Y YA ESTA
        k = 14  # Grado promedio de los nodos
        p = 0.6  # Probabilidad de "rewiring"
        self.graph1 = nx.watts_strogatz_graph(N, k, p)
        m = 6  # Número de conexiones iniciales para cada nodo nuevo
        self.graph2 = nx.barabasi_albert_graph(N, m)
        #INICIALIZO LOS ESTADOS AL AZAR EN LA RED CON CONEXIONES YA CREADAS
        estados = ['V'] * V + ['S'] * S + ['Sn'] * Sn + ['I'] * I + ['I_v'] * I_v +['R'] * R
        random.shuffle(estados)


        for i, nodo in enumerate(self.graph1.nodes()):
            estado = estados[i]
            self.graph1.nodes[nodo]['state'] = estado
            self.graph2.nodes[nodo]['state'] = estado


        #Listas de estados y vectores de rates de infección
        self.Snodos=[]
        self.Snnodos=[]
        self.Vnodos=[]
        self.Inodos=[]
        self.I_vnodos=[]
        self.Rnodos=[]
        #RATES, QUE VAN DE UN GRUPO PROVOCADO POR OTRO GRUPO, ASÍ SE ELEGIRÁ AL QUE MAS RATE TENGA COMO INFECTADO
        self.SRATESI=[]
        self.SRATESI_v=[]
        self.VRATESI=[]
        self.SnRATESI=[]
        self.VRATESI_v=[]
        self.SnRATESI_v=[]
        self.SRATESSn=[]
        self.SnRATESS=[]
        #Inicializo todas las listas con los nodos de cada lista
        for nodo in self.graph1.nodes():
            if self.graph1.nodes[nodo]['state'] == 'S':
                self.Snodos.append(nodo)
            elif self.graph1.nodes[nodo]['state'] == 'Sn':
                self.Snnodos.append(nodo)
            elif self.graph1.nodes[nodo]['state'] == 'V':
                self.Vnodos.append(nodo)
            elif self.graph1.nodes[nodo]['state'] == 'R':
                self.Rnodos.append(nodo)
            elif self.graph1.nodes[nodo]['state'] == 'I':
                self.Inodos.append(nodo)
            elif self.graph1.nodes[nodo]['state'] == 'I_v':
                self.I_vnodos.append(nodo)



    #Tendremos las siguientes reacciones
    # 1      V+I_v-gammav1>2I_v           
    #  2     V+I-gammav2>I_v+I     
    #   3    S+I-gammas1>2I    
    #  4     S+I_v-gammas2>I+I_v   
    # 5      Sn+I-gammasn1>2I     
    #  6     Sn+I_v-gammasn2>I+I_v
    #   7    S-alfa>V       
    #  8     S-beta>Sn       
    #   9    S-sigma>S(puede ser cero)      
    #    10  I-nu>R      
    #    11  I_v-nuv>R_v
    #        Usare rate 1 2 3 y así en este orden.
    #CON TEORÍA DE REDES
    def rates1(self):
        #parte de los infectados
        r1=r2=r3=r4=r5=r6=r7=r10=r11=0
        self.SRATESI=[]
        self.SRATESI_v=[]
        self.VRATESI=[]
        self.SnRATESI=[]
        self.VRATESI_v=[]
        self.SnRATESI_v=[]
        
        
        


        for nodo in self.Snodos:
            vecinos=list(self.graph1.neighbors(nodo))
            SRATESI=SRATESI_v=0
            for vecino in vecinos:
                if vecino in self.Inodos:
                    SRATESI+=self.gammas1                    
                elif vecino in self.I_vnodos:
                    SRATESI_v+=self.gammas2
            self.SRATESI.append(SRATESI)
            self.SRATESI_v.append(SRATESI_v)
            r3+=SRATESI
            r4+=SRATESI_v


        for nodo in self.Vnodos:    
            vecinos=list(self.graph1.neighbors(nodo))           
            VRATESI=VRATESI_v=0
            for vecino in vecinos:
                if vecino in self.Inodos:
                    VRATESI+=self.gammav2                    
                elif vecino in self.I_vnodos:
                    VRATESI_v+=self.gammav1
            self.VRATESI.append(VRATESI)
            self.VRATESI_v.append(VRATESI_v)
            r2+=VRATESI
            r1+=VRATESI_v


        for nodo in self.Snnodos:            
            vecinos=list(self.graph1.neighbors(nodo))
            SnRATESI=SnRATESI_v=0
            for vecino in vecinos:
                if vecino in self.Inodos:
                    SnRATESI+=self.gammasn1                    
                elif vecino in self.I_vnodos:
                    SnRATESI_v+=self.gammasn2
            self.SnRATESI.append(SnRATESI)
            self.SnRATESI_v.append(SnRATESI_v)
            r5+=SnRATESI
            r6+=SnRATESI_v



        
        
        r10=self.nu*self.I
        r11=self.nuv*self.I_v   
        return r1,r2,r3,r4,r5,r6,r10,r11

    #DINAMICA SOCIAL
    def rates2(self):
        r8=r9=0
        self.SRATESSn=[]
        self.SnRATESS=[]
        for nodo in self.Snodos:            
            vecinos=list(self.graph2.neighbors(nodo))
            SRATESSn=0
            for vecino in vecinos:
                if vecino in self.Snnodos:
                    SRATESSn+=self.beta      
            self.SRATESSn.append(SRATESSn)            
            r8+=SRATESSn

            
                
        for nodo in self.Snnodos:     
            vecinos=list(self.graph2.neighbors(nodo))
            SnRATESS=0
            for vecino in vecinos:
                if vecino in self.Snodos:
                    SnRATESS+=self.sigma    
            self.SnRATESS.append(SnRATESS)            
            r9+=SnRATESS
       
        return r8,r9



    #Tendremos las siguientes reacciones
    # 1      V+I_v-gammav1>2I_v           
    #  2     V+I-gammav2>I_v+I     
    #   3    S+I-gammas1>2I    
    #  4     S+I_v-gammas2>I+I_v   
    # 5      Sn+I-gammasn1>2I     
    #  6     Sn+I_v-gammasn2>I+I_v
    #   7    S-alfa>V       
    #  8     S-beta>Sn       
    #   9    Sn-sigma>S(puede ser cero)      
    #    10  I-nu>R      
    #    11  I_v-nuv>R_v
    #        Usare rate 1 2 3 y así en este orden.
        #CON TEORÍA DE REDES
    def Simular(self):
            self.r1,self.r2,self.r3,self.r4,self.r5,self.r6,self.r10,self.r11=self.rates1()
            self.r8,self.r9=self.rates2()
            iteracion=0
            while (self.R!=self.N):
                # Calcular las tasas de infección y recuperación
                #if iteracion%10000==0:
                 #   self.r1,self.r2,self.r3,self.r4,self.r5,self.r6,self.r7,self.r10,self.r11=self.rates1()
                 #   self.r8,self.r9=self.rates2()
                #iteracion+=1
                #if self.Sn==0 :
                    #hola
                    #hola
                    #a=2
                #r1,r2,r3,r4,r5,r6,r7,r10,r11 = self.rates1()

                

                if self.r1<1.E-4:
                    self.r1=0
                if self.r2<1.E-4:
                    self.r2=0
                if self.r3<1.E-4:
                    self.r3=0
                if self.r4<1.E-4:
                    self.r4=0
                if self.r5<1.E-4:
                    self.r5=0
                if self.r6<1.E-4:
                    self.r6=0
                if self.r8<1.E-4:
                    self.r8=0
                if self.r9<1.E-4:
                    self.r9=0
                if self.r10<1.E-4:
                    self.r10=0
                if self.r11<1.E-4:
                    self.r11=0


                # Calcular el tiempo hasta el próximo evento
                tr = self.r1+self.r2+self.r3+self.r4+self.r5+self.r6+self.r10+self.r11
                if tr==0:
                    break
                
                
                delta_t = -np.log(np.random.random())/tr
            # Elegir aleatoriamente el tipo de evento que ocurre
                event = np.random.choice(["r1","r2","r3","r4","r5","r6","r10","r11"], p=[self.r1/tr,self.r2/tr,self.r3/tr,self.r4/tr,self.r5/tr,self.r6/tr,self.r10/tr,self.r11/tr])

                #if self.r4*self.r2*self.r6<=0  and self.S<=100 :
                    #a=3
                

            # Actualizar las poblaciones y el tiempo
                #EN ESTE CASO SE TOMA UN VACUNADO AL AZAR, EL INDICE DE vNODOS SERÁ EL QUE TENGA EL VRATE MAS GRANDE
                #SE ELIMINA DE VNODOS Y DE INCLUYE EN i_V NODOS. Y SE ELIMINAN Y RESTAN LOS V RATES QUE SON SUYOS
                #SE AÑADE LA PROBABILIDAD DE RECUPERARSE.Y SE AUMENTAN LOS RATES DE INFECCIÓN
                if event == "r1":
                    self.V -= 1
                    self.I_v += 1
                    indice=self.VRATESI_v.index(max(self.VRATESI_v))
                    eleccion=self.Vnodos[indice]                    
                    self.Vnodos.remove(eleccion)
                    self.r1-=self.VRATESI_v[indice]
                    self.VRATESI_v.remove(self.VRATESI_v[indice])
                    self.r2-=self.VRATESI[indice]
                    self.VRATESI.remove(self.VRATESI[indice])
                    self.I_vnodos.append(eleccion)
                    self.r11+=self.nuv
                    vecinos=list(self.graph1.neighbors(eleccion))           
                    
                    for vecino in vecinos:
                        if vecino in self.Vnodos:
                            self.VRATESI_v[self.Vnodos.index(vecino)]+=self.gammav1 
                            self.r1+=self.gammav1                    
                        elif vecino in self.Snodos:
                            self.SRATESI_v[self.Snodos.index(vecino)]+=self.gammas2
                            self.r4+=self.gammas2
                        elif vecino in self.Snnodos:
                            self.SnRATESI_v[self.Snnodos.index(vecino)]+=self.gammasn2
                            self.r6+=self.gammasn2  
                    
                    

                elif event == "r2":
                    self.V -= 1
                    self.I_v += 1
                    indice=self.VRATESI.index(max(self.VRATESI))
                    eleccion=self.Vnodos[indice]                    
                    self.Vnodos.remove(eleccion)
                    self.I_vnodos.append(eleccion)
                    self.r1-=self.VRATESI_v[indice]
                    self.r2-=self.VRATESI[indice]
                    self.VRATESI_v.remove(self.VRATESI_v[indice])
                    self.VRATESI.remove(self.VRATESI[indice])
                    self.r11+=self.nuv

                    vecinos=list(self.graph1.neighbors(eleccion))           
                    
                    for vecino in vecinos:
                        if vecino in self.Vnodos:
                            self.VRATESI_v[self.Vnodos.index(vecino)]+=self.gammav1 
                            self.r1+=self.gammav1                    
                        elif vecino in self.Snodos:
                            self.SRATESI_v[self.Snodos.index(vecino)]+=self.gammas2
                            self.r4+=self.gammas2
                        elif vecino in self.Snnodos:
                            self.SnRATESI_v[self.Snnodos.index(vecino)]+=self.gammasn2
                            self.r6+=self.gammasn2
                    


                elif event == "r3":
                    self.S -= 1
                    self.I += 1
                    if len(self.SRATESI)==0:
                        continue
                    indice=self.SRATESI.index(max(self.SRATESI))
                    eleccion=self.Snodos[indice]                   
                    self.Snodos.remove(eleccion)
                    self.Inodos.append(eleccion)
                    self.r4-=self.SRATESI_v[indice]
                    self.r3-=self.SRATESI[indice]
                    self.r8-=self.SRATESSn[indice]
                    self.SRATESI.remove(self.SRATESI[indice])
                    self.SRATESI_v.remove(self.SRATESI_v[indice])
                    self.SRATESSn.remove(self.SRATESSn[indice])
                    self.r10+=self.nu
                    #self.r7-=self.alfa

                    vecinos=list(self.graph1.neighbors(eleccion))           
                    
                    for vecino in vecinos:
                        if vecino in self.Vnodos:
                            self.VRATESI[self.Vnodos.index(vecino)]+=self.gammav2
                            self.r2+=self.gammav2                    
                        elif vecino in self.Snodos:
                            self.SRATESI[self.Snodos.index(vecino)]+=self.gammas1
                            self.r3+=self.gammas1
                        elif vecino in self.Snnodos:
                            self.SnRATESI[self.Snnodos.index(vecino)]+=self.gammasn1
                            self.r5+=self.gammasn1
                    


                elif event == "r4":
                    self.S -= 1
                    self.I += 1       
                    indice=self.SRATESI_v.index(max(self.SRATESI_v))
                    eleccion=self.Snodos[indice]                     
                    self.Snodos.remove(eleccion)
                    self.Inodos.append(eleccion)
                    self.r4-=self.SRATESI_v[indice]
                    self.r3-=self.SRATESI[indice]
                    self.r8-=self.SRATESSn[indice]
                    self.SRATESI.remove(self.SRATESI[indice])
                    self.SRATESI_v.remove(self.SRATESI_v[indice])
                    self.SRATESSn.remove(self.SRATESSn[indice])
                    self.r10+=self.nu
                    #self.r7-=self.alfa

                    vecinos=list(self.graph1.neighbors(eleccion))           
                    
                    for vecino in vecinos:
                        if vecino in self.Vnodos:
                            self.VRATESI[self.Vnodos.index(vecino)]+=self.gammav2
                            self.r2+=self.gammav2                    
                        elif vecino in self.Snodos:
                            self.SRATESI[self.Snodos.index(vecino)]+=self.gammas1
                            self.r3+=self.gammas1
                        elif vecino in self.Snnodos:
                            self.SnRATESI[self.Snnodos.index(vecino)]+=self.gammasn1
                            self.r5+=self.gammasn1
                    

                elif event == "r5":
                    self.Sn -= 1
                    self.I += 1      
                    #if self.r6==0:
                        #a=4
                    indice=self.SnRATESI.index(max(self.SnRATESI))
                    eleccion=self.Snnodos[indice]                    
                    self.Snnodos.remove(eleccion)
                    self.Inodos.append(eleccion)
                    self.r6-=self.SnRATESI_v[indice]
                    self.r5-=self.SnRATESI[indice]
                    self.r9-=self.SnRATESS[indice]
                    self.SnRATESI.remove(self.SnRATESI[indice])
                    self.SnRATESI_v.remove(self.SnRATESI_v[indice])
                    self.SnRATESS.remove(self.SnRATESS[indice])
                    self.r10+=self.nu
                    vecinos=list(self.graph1.neighbors(eleccion))           
                    
                    for vecino in vecinos:
                        if vecino in self.Vnodos:
                            self.VRATESI[self.Vnodos.index(vecino)]+=self.gammav2
                            self.r2+=self.gammav2                    
                        elif vecino in self.Snodos:
                            self.SRATESI[self.Snodos.index(vecino)]+=self.gammas1
                            self.r3+=self.gammas1
                        elif vecino in self.Snnodos:
                            self.SnRATESI[self.Snnodos.index(vecino)]+=self.gammasn1
                            self.r5+=self.gammasn1
                    



                elif event == "r6":
                    self.Sn -= 1
                    self.I += 1    
                    indice=self.SnRATESI_v.index(max(self.SnRATESI_v))
                    eleccion=self.Snnodos[indice]  
                    self.Snnodos.remove(eleccion)
                    self.Inodos.append(eleccion)
                    self.r6-=self.SnRATESI_v[indice]
                    self.r5-=self.SnRATESI[indice]
                    self.r9-=self.SnRATESS[indice]
                    self.SnRATESI.remove(self.SnRATESI[indice])
                    self.SnRATESI_v.remove(self.SnRATESI_v[indice])
                    self.SnRATESS.remove(self.SnRATESS[indice])
                    self.r10+=self.nu
                    vecinos=list(self.graph1.neighbors(eleccion))           
                    
                    for vecino in vecinos:
                        if vecino in self.Vnodos:
                            self.VRATESI[self.Vnodos.index(vecino)]+=self.gammav2
                            self.r2+=self.gammav2                    
                        elif vecino in self.Snodos:
                            self.SRATESI[self.Snodos.index(vecino)]+=self.gammas1
                            self.r3+=self.gammas1
                        elif vecino in self.Snnodos:
                            self.SnRATESI[self.Snnodos.index(vecino)]+=self.gammasn1
                            self.r5+=self.gammasn1
                    



                
                    




                
                elif event == "r10":
                    self.I -= 1
                    self.R += 1
                    eleccion=random.choice(self.Inodos)                    
                    self.Inodos.remove(eleccion)
                    self.Rnodos.append(eleccion)
                    vecinos=list(self.graph1.neighbors(eleccion))           
                    self.r10-=self.nu
                    for vecino in vecinos:
                        if vecino in self.Vnodos:
                            self.VRATESI[self.Vnodos.index(vecino)]-=self.gammav2
                            self.r2-=self.gammav2                    
                        elif vecino in self.Snodos:
                            self.SRATESI[self.Snodos.index(vecino)]-=self.gammas1
                            self.r3-=self.gammas1
                        elif vecino in self.Snnodos:
                            self.SnRATESI[self.Snnodos.index(vecino)]-=self.gammasn1
                            self.r5-=self.gammasn1
                    

                else:
                    self.I_v -= 1
                    self.R += 1    
                    eleccion=random.choice(self.I_vnodos)                    
                    self.I_vnodos.remove(eleccion)
                    self.Rnodos.append(eleccion)
                    self.r11-=self.nuv
                    vecinos=list(self.graph1.neighbors(eleccion))           
                    
                    for vecino in vecinos:
                        if vecino in self.Vnodos:
                            self.VRATESI_v[self.Vnodos.index(vecino)]-=self.gammav1 
                            self.r1-=self.gammav1                    
                        elif vecino in self.Snodos:
                            self.SRATESI_v[self.Snodos.index(vecino)]-=self.gammas2
                            self.r4-=self.gammas2
                        elif vecino in self.Snnodos:
                            self.SnRATESI_v[self.Snnodos.index(vecino)]-=self.gammasn2
                            self.r6-=self.gammasn2
                    
                    



                #r8,r9=self.rates2()
                tr2 =self.r8+self.r9
                # Elegir aleatoriamente el tipo de evento que ocurre
                if tr2!=0:
                    event2 = np.random.choice(["r8","r9"], p=[self.r8/tr2,self.r9/tr2])
              
                    if event2 == "r8" :
                        self.S -= 1
                        self.Sn += 1
                        indice=self.SRATESSn.index(max(self.SRATESSn))
                        eleccion=self.Snodos[indice]                        
                        self.Snodos.remove(eleccion)
                        self.Snnodos.append(eleccion)
                        self.r4-=self.SRATESI_v[indice]
                        self.r3-=self.SRATESI[indice]
                        self.r8-=self.SRATESSn[indice]
                        self.SRATESI.remove(self.SRATESI[indice])
                        self.SRATESI_v.remove(self.SRATESI_v[indice])
                        self.SRATESSn.remove(self.SRATESSn[indice])
                        #self.r7-=self.alfa
                       
                        vecinos=list(self.graph1.neighbors(eleccion))           
                        SnRATESI=SnRATESI_v=SnRATESS=0
                        for vecino in vecinos:
                            if vecino in self.Inodos:
                                SnRATESI+=self.gammasn1 
                                self.r5+=self.gammasn1                   
                            elif vecino in self.I_vnodos:
                                SnRATESI_v+=self.gammasn2
                                self.r6+=self.gammasn2
                        vecinos=list(self.graph2.neighbors(eleccion)) 
                        for vecino in vecinos:
                            if vecino in self.Snodos:
                                SnRATESS+=self.sigma
                                self.r9+=self.sigma
                        self.SnRATESI.append(SnRATESI)
                        self.SnRATESI_v.append(SnRATESI_v)
                        self.SnRATESS.append(SnRATESS)
                        
                        

                    else :
                        self.Sn -= 1
                        self.S += 1    
                        indice=self.SnRATESS.index(max(self.SnRATESS))    
                        eleccion=self.Snnodos[indice]                   
                        self.Snnodos.remove(eleccion)
                        self.Snodos.append(eleccion)
                        self.r6-=self.SnRATESI_v[indice]
                        self.r5-=self.SnRATESI[indice]
                        self.r9-=self.SnRATESS[indice]   
                        self.SnRATESI.remove(self.SnRATESI[indice])
                        self.SnRATESI_v.remove(self.SnRATESI_v[indice]) 
                        self.SnRATESS.remove(self.SnRATESS[indice])
                        #self.r7+=self.alfa
                                            
                        vecinos=list(self.graph1.neighbors(eleccion))           
                        SRATESI=SRATESI_v=SRATESSn=0
                        for vecino in vecinos:
                            if vecino in self.Inodos:
                                SRATESI+=self.gammas1 
                                self.r3+=self.gammas1                   
                            elif vecino in self.I_vnodos:
                                SRATESI_v+=self.gammas2
                                self.r4+=self.gammas2
                        vecinos=list(self.graph2.neighbors(eleccion)) 
                        for vecino in vecinos:
                            if vecino in self.Snnodos:
                                SRATESSn+=self.beta
                                self.r8+=self.beta
                        self.SRATESI.append(SRATESI)
                        self.SRATESI_v.append(SRATESI_v)
                        self.SRATESSn.append(SRATESSn)
                        




                if self.S!=0 and self.t>self.tiempovacuna:
                    for i in (0,int(self.alfa*self.N*delta_t)):
                        if len(self.Snodos)==0:
                            break
                        self.S -= 1
                        self.V += 1
                        eleccion=random.choice(self.Snodos)  
                        indice=self.Snodos.index(eleccion)                  
                        self.Snodos.remove(eleccion)
                        self.Vnodos.append(eleccion)
                        self.r4-=self.SRATESI_v[indice]
                        self.r3-=self.SRATESI[indice]
                        self.r8-=self.SRATESSn[indice]
                        self.SRATESI.remove(self.SRATESI[indice])
                        self.SRATESI_v.remove(self.SRATESI_v[indice])
                        self.SRATESSn.remove(self.SRATESSn[indice])
                    
                        vecinos=list(self.graph1.neighbors(eleccion))           
                        VRATESI=VRATESI_v=0
                        for vecino in vecinos:
                            if vecino in self.Inodos:
                                VRATESI+=self.gammav2 
                                self.r2+=self.gammav2                   
                            elif vecino in self.I_vnodos:
                                VRATESI_v+=self.gammav1
                                self.r1+=self.gammav1
                        self.VRATESI.append(VRATESI)
                        self.VRATESI_v.append(VRATESI_v)
                        
                        


                self.t += delta_t
                #print(self.t)

                # Almacenar los resultados
                self.time_list.append(self.t)
                self.S_list.append(self.S)
                self.Sn_list.append(self.Sn)
                self.V_list.append(self.V)
                self.I_list.append(self.I)
                self.I_v_list.append(self.I_v)
                self.R_list.append(self.R)






    def Graficar1(self):
        # Graficar los resultados
        plt.clf()
        #sumo las listas 
        Stlist = [x + y for x, y in zip(self.S_list,self.Sn_list)]
        ItList = [x + y for x, y in zip(self.I_list,self.I_v_list)]
        plt.plot(self.time_list, Stlist , label="Susceptibles")
        plt.plot(self.time_list, self.V_list, label="Vacunados sanos")
        plt.plot(self.time_list, ItList, label="Infectados")        
        plt.plot(self.time_list, self.R_list, label="Recuperados")
        #plt.plot(time_list, R_list, label="Recuperados")
        plt.xlabel("Tiempo")
        plt.ylabel("Número de individuos")
        #texto="Figura_{0}_{1}_\n{2}_{3}_{4}\n_{5}_{6}_{7}\n_{8}_{9}_\n{10}.png".format(self.gammav1,self.gammav2,self.gammas1,self.gammas2,self.gammasn1,self.gammasn2,self.alfa,self.beta,self.sigma,self.nu,self.nuv)
        #plt.text(4.5, 9, texto, ha='right',va='top')
        plt.legend()
        # Crear la carpeta donde se va aguardar si no existe
        if not os.path.exists("Imagenes"):
            os.makedirs("Imagenes")
        if not os.path.exists(os.path.join("Imagenes", "PROTOTIPO3")):
            os.makedirs(os.path.join("Imagenes", "PROTOTIPO3"))

        # Guardar la figura en la carpeta "imagenes" dentro de "proyecto"
        filepath = os.path.join("Imagenes", "PROTOTIPO3", "Resumen_{0}_{1}_{2}_{3}..png".format(self.alfa,self.beta,self.sigma,self.tiempovacuna))
        plt.savefig(filepath)
        #print('Simulacion1 realizada.')
        


    def Graficar2(self):
        # Graficar los resultados
        plt.clf()
        #sumo las listas 
        
        plt.plot(self.time_list, self.Sn_list , label="Susceptibles antivacunas")
        plt.plot(self.time_list, self.S_list , label="Susceptibles provacunas")
        plt.plot(self.time_list, self.V_list, label="Vacunados sanos")
        plt.plot(self.time_list, self.I_list, label="Infectados no vacunados")        
        plt.plot(self.time_list, self.I_v_list, label="Infectados vacunados") 
        plt.plot(self.time_list, self.R_list, label="Recuperados")
        #plt.plot(time_list, R_list, label="Recuperados")
        plt.xlabel("Tiempo")
        plt.ylabel("Número de individuos")
        #texto="Figura_{0}_{1}_\n{2}_{3}_{4}\n_{5}_{6}_{7}\n_{8}_{9}_\n{10}.png".format(self.gammav1,self.gammav2,self.gammas1,self.gammas2,self.gammasn1,self.gammasn2,self.alfa,self.beta,self.sigma,self.nu,self.nuv)
        #plt.text(4.5, 9, texto, ha='right',va='top')
        plt.legend()
        # Crear la carpeta donde se va aguardar si no existe
        if not os.path.exists("Imagenes"):
            os.makedirs("Imagenes")
        if not os.path.exists(os.path.join("Imagenes", "PROTOTIPO3")):
            os.makedirs(os.path.join("Imagenes", "PROTOTIPO3"))

        # Guardar la figura en la carpeta "imagenes" dentro de "proyecto"
        filepath = os.path.join("Imagenes", "PROTOTIPO3", "Todos_{0}_{1}_{2}_{3}.png".format(self.alfa,self.beta,self.sigma,self.tiempovacuna))
        plt.savefig(filepath)
        #print('Simulacion2 realizada.')
        

#PROTOTIPO3, AHORA INTENTO optimizar TEORÍA DE REDES

class Prototipo3mv:

    #de momento se supone se empieza sin vacunados
    def __init__(self,gammav1,gammav2,gammas1,gammas2,gammasn1,gammasn2,alfa, beta,sigma,nu,nuv,vitality, N,V, S,Sn,I,R,t,tvacuna,tmax):
        self.gammav1=gammav1
        self.gammav2=gammav2
        self.gammas1=gammas1
        self.gammas2=gammas2
        self.gammasn1=gammasn1
        self.gammasn2=gammasn2
        self.tmax=tmax
        self.vitality=vitality
        self.alfa=alfa
        self.sigma=sigma
        self.nu=nu
        self.nuv=nuv
        self.beta=beta
        #VARIABLES QUE USAREMOS PARA GRAFICAR LOS RESULTADPS
        self.N=N
        self.t=t
        self.S=S
        self.Sn=Sn
        
        self.V=V
        self.I=I
        I_v=0
        self.I_v=I_v
        self.R=R
        self.time_list=[t]        
        self.S_list = [S]
        self.I_list = [I]
        self.Sn_list = [Sn]
        self.V_list = [V]
        self.I_v_list = [I_v]
        self.R_list=[R]
        self.tiempovacuna=tvacuna
        self.r1=self.r2=self.r3=self.r4=self.r5=self.r6=self.r7=self.r8=self.r9=self.r10=self.r11=0
        #REDES A USAR 

        # Parámetros DE LAS REDES, SUPONGO QUE NO NOS INTERESA VER COMO CAMBIAN EL RESULTADO
        # ASI QUE PONEMOS UNOS Y YA ESTA
        k = 14  # Grado promedio de los nodos
        p = 0.6  # Probabilidad de "rewiring"
        self.graph1 = nx.watts_strogatz_graph(N, k, p)
        m = 6  # Número de conexiones iniciales para cada nodo nuevo
        self.graph2 = nx.barabasi_albert_graph(N, m)
        #INICIALIZO LOS ESTADOS AL AZAR EN LA RED CON CONEXIONES YA CREADAS
        estados = ['V'] * V + ['S'] * S + ['Sn'] * Sn + ['I'] * I + ['I_v'] * I_v +['R'] * R
        random.shuffle(estados)


        for i, nodo in enumerate(self.graph1.nodes()):
            estado = estados[i]
            self.graph1.nodes[nodo]['state'] = estado
            self.graph2.nodes[nodo]['state'] = estado


        #Listas de estados y vectores de rates de infección
        self.Snodos=[]
        self.Snnodos=[]
        self.Vnodos=[]
        self.Inodos=[]
        self.I_vnodos=[]
        self.Rnodos=[]
        #RATES, QUE VAN DE UN GRUPO PROVOCADO POR OTRO GRUPO, ASÍ SE ELEGIRÁ AL QUE MAS RATE TENGA COMO INFECTADO
        self.SRATESI=[]
        self.SRATESI_v=[]
        self.VRATESI=[]
        self.SnRATESI=[]
        self.VRATESI_v=[]
        self.SnRATESI_v=[]
        self.SRATESSn=[]
        self.SnRATESS=[]
        #Inicializo todas las listas con los nodos de cada lista
        for nodo in self.graph1.nodes():
            if self.graph1.nodes[nodo]['state'] == 'S':
                self.Snodos.append(nodo)
            elif self.graph1.nodes[nodo]['state'] == 'Sn':
                self.Snnodos.append(nodo)
            elif self.graph1.nodes[nodo]['state'] == 'V':
                self.Vnodos.append(nodo)
            elif self.graph1.nodes[nodo]['state'] == 'R':
                self.Rnodos.append(nodo)
            elif self.graph1.nodes[nodo]['state'] == 'I':
                self.Inodos.append(nodo)
            elif self.graph1.nodes[nodo]['state'] == 'I_v':
                self.I_vnodos.append(nodo)



    #Tendremos las siguientes reacciones
    # 1      V+I_v-gammav1>2I_v           
    #  2     V+I-gammav2>I_v+I     
    #   3    S+I-gammas1>2I    
    #  4     S+I_v-gammas2>I+I_v   
    # 5      Sn+I-gammasn1>2I     
    #  6     Sn+I_v-gammasn2>I+I_v
    #   7    S-alfa>V       
    #  8     S-beta>Sn       
    #   9    S-sigma>S(puede ser cero)      
    #    10  I-nu>R      
    #    11  I_v-nuv>R_v
    #        Usare rate 1 2 3 y así en este orden.
    #CON TEORÍA DE REDES
    def rates1(self):
        #parte de los infectados
        r1=r2=r3=r4=r5=r6=r7=r10=r11=0
        self.SRATESI=[]
        self.SRATESI_v=[]
        self.VRATESI=[]
        self.SnRATESI=[]
        self.VRATESI_v=[]
        self.SnRATESI_v=[]
        
        
        


        for nodo in self.Snodos:
            vecinos=list(self.graph1.neighbors(nodo))
            SRATESI=SRATESI_v=0
            for vecino in vecinos:
                if vecino in self.Inodos:
                    SRATESI+=self.gammas1                    
                elif vecino in self.I_vnodos:
                    SRATESI_v+=self.gammas2
            self.SRATESI.append(SRATESI)
            self.SRATESI_v.append(SRATESI_v)
            r3+=SRATESI
            r4+=SRATESI_v


        for nodo in self.Vnodos:    
            vecinos=list(self.graph1.neighbors(nodo))           
            VRATESI=VRATESI_v=0
            for vecino in vecinos:
                if vecino in self.Inodos:
                    VRATESI+=self.gammav2                    
                elif vecino in self.I_vnodos:
                    VRATESI_v+=self.gammav1
            self.VRATESI.append(VRATESI)
            self.VRATESI_v.append(VRATESI_v)
            r2+=VRATESI
            r1+=VRATESI_v


        for nodo in self.Snnodos:            
            vecinos=list(self.graph1.neighbors(nodo))
            SnRATESI=SnRATESI_v=0
            for vecino in vecinos:
                if vecino in self.Inodos:
                    SnRATESI+=self.gammasn1                    
                elif vecino in self.I_vnodos:
                    SnRATESI_v+=self.gammasn2
            self.SnRATESI.append(SnRATESI)
            self.SnRATESI_v.append(SnRATESI_v)
            r5+=SnRATESI
            r6+=SnRATESI_v



        
        
        r10=self.nu*self.I
        r11=self.nuv*self.I_v   
        return r1,r2,r3,r4,r5,r6,r10,r11

    #DINAMICA SOCIAL
    def rates2(self):
        r8=r9=0
        self.SRATESSn=[]
        self.SnRATESS=[]
        for nodo in self.Snodos:            
            vecinos=list(self.graph2.neighbors(nodo))
            SRATESSn=0
            for vecino in vecinos:
                if vecino in self.Snnodos:
                    SRATESSn+=self.beta      
            self.SRATESSn.append(SRATESSn)            
            r8+=SRATESSn

            
                
        for nodo in self.Snnodos:     
            vecinos=list(self.graph2.neighbors(nodo))
            SnRATESS=0
            for vecino in vecinos:
                if vecino in self.Snodos:
                    SnRATESS+=self.sigma    
            self.SnRATESS.append(SnRATESS)            
            r9+=SnRATESS
       
        return r8,r9



    #Tendremos las siguientes reacciones
    # 1      V+I_v-gammav1>2I_v           
    #  2     V+I-gammav2>I_v+I     
    #   3    S+I-gammas1>2I    
    #  4     S+I_v-gammas2>I+I_v   
    # 5      Sn+I-gammasn1>2I     
    #  6     Sn+I_v-gammasn2>I+I_v
    #   7    S-alfa>V       
    #  8     S-beta>Sn       
    #   9    Sn-sigma>S(puede ser cero)      
    #    10  I-nu>R      
    #    11  I_v-nuv>R_v
    #        Usare rate 1 2 3 y así en este orden.
        #CON TEORÍA DE REDES
    def Simular(self):
            self.r1,self.r2,self.r3,self.r4,self.r5,self.r6,self.r10,self.r11=self.rates1()
            self.r8,self.r9=self.rates2()
            iteracion=0
            while (self.t<self.tmax):
                # Calcular las tasas de infección y recuperación
                #if iteracion%10000==0:
                 #   self.r1,self.r2,self.r3,self.r4,self.r5,self.r6,self.r7,self.r10,self.r11=self.rates1()
                 #   self.r8,self.r9=self.rates2()
                #iteracion+=1
                #if self.Sn==0 :
                    #hola
                    #hola
                    #a=2
                #r1,r2,r3,r4,r5,r6,r7,r10,r11 = self.rates1()

                

                if self.r1<1.E-4:
                    self.r1=0
                if self.r2<1.E-4:
                    self.r2=0
                if self.r3<1.E-4:
                    self.r3=0
                if self.r4<1.E-4:
                    self.r4=0
                if self.r5<1.E-4:
                    self.r5=0
                if self.r6<1.E-4:
                    self.r6=0
                if self.r8<1.E-4:
                    self.r8=0
                if self.r9<1.E-4:
                    self.r9=0
                if self.r10<1.E-4:
                    self.r10=0
                if self.r11<1.E-4:
                    self.r11=0

                if len(self.Vnodos)!=len(self.VRATESI)!=len(self.VRATESI_v):
                    self.r1,self.r2,self.r3,self.r4,self.r5,self.r6,self.r10,self.r11=self.rates1()
                    self.r8,self.r9=self.rates2()
                if len(self.Snodos)!=len(self.SRATESI)!=len(self.SRATESI_v)!=len(self.SRATESSn):
                    self.r1,self.r2,self.r3,self.r4,self.r5,self.r6,self.r10,self.r11=self.rates1()
                    self.r8,self.r9=self.rates2()
                if len(self.Snnodos)!=len(self.SnRATESI)!=len(self.SnRATESI_v)!=len(self.SnRATESS):
                    self.r1,self.r2,self.r3,self.r4,self.r5,self.r6,self.r10,self.r11=self.rates1()
                    self.r8,self.r9=self.rates2()
                if self.I!=len(self.Inodos):
                    self.r1,self.r2,self.r3,self.r4,self.r5,self.r6,self.r10,self.r11=self.rates1()
                    self.r8,self.r9=self.rates2()
                


                # Calcular el tiempo hasta el próximo evento
                tr = self.r1+self.r2+self.r3+self.r4+self.r5+self.r6+self.r10+self.r11
                if tr==0:
                    self.r1,self.r2,self.r3,self.r4,self.r5,self.r6,self.r10,self.r11=self.rates1()
                    self.r8,self.r9=self.rates2()
                    if self.r1<1.E-1:
                        self.r1=0
                    if self.r2<1.E-1:
                        self.r2=0
                    if self.r3<1.E-1:
                        self.r3=0
                    if self.r4<1.E-1:
                        self.r4=0
                    if self.r5<1.E-1:
                        self.r5=0
                    if self.r6<1.E-1:
                        self.r6=0
                    if self.r8<1.E-1:
                        self.r8=0
                    if self.r9<1.E-1:
                        self.r9=0
                    if self.r10<1.E-1:
                        self.r10=0
                    if self.r11<1.E-1:
                        self.r11=0
                    
                    tr = self.r1+self.r2+self.r3+self.r4+self.r5+self.r6+self.r10+self.r11
                    if tr==0:
                        break
                
                
                delta_t = -np.log(np.random.random())/tr
            # Elegir aleatoriamente el tipo de evento que ocurre
                event = np.random.choice(["r1","r2","r3","r4","r5","r6","r10","r11"], p=[self.r1/tr,self.r2/tr,self.r3/tr,self.r4/tr,self.r5/tr,self.r6/tr,self.r10/tr,self.r11/tr])

                #if self.r4*self.r2*self.r6<=0  and self.S<=100 :
                    #a=3
                

            # Actualizar las poblaciones y el tiempo
                #EN ESTE CASO SE TOMA UN VACUNADO AL AZAR, EL INDICE DE vNODOS SERÁ EL QUE TENGA EL VRATE MAS GRANDE
                #SE ELIMINA DE VNODOS Y DE INCLUYE EN i_V NODOS. Y SE ELIMINAN Y RESTAN LOS V RATES QUE SON SUYOS
                #SE AÑADE LA PROBABILIDAD DE RECUPERARSE.Y SE AUMENTAN LOS RATES DE INFECCIÓN
                if event == "r1":
                    if self.V==0:
                        self.r1=0 
                        continue
                    self.V -= 1
                    self.I_v += 1
                    indice=self.VRATESI_v.index(max(self.VRATESI_v))
                    eleccion=self.Vnodos[indice]                    
                    self.Vnodos.remove(eleccion)
                    self.r1-=self.VRATESI_v[indice]
                    self.VRATESI_v.remove(self.VRATESI_v[indice])
                    self.r2-=self.VRATESI[indice]
                    self.VRATESI.remove(self.VRATESI[indice])
                    self.I_vnodos.append(eleccion)
                    self.r11+=self.nuv
                    vecinos=list(self.graph1.neighbors(eleccion))           
                    
                    for vecino in vecinos:
                        if vecino in self.Vnodos:
                            self.VRATESI_v[self.Vnodos.index(vecino)]+=self.gammav1 
                            self.r1+=self.gammav1                    
                        elif vecino in self.Snodos:
                            self.SRATESI_v[self.Snodos.index(vecino)]+=self.gammas2
                            self.r4+=self.gammas2
                        elif vecino in self.Snnodos:
                            self.SnRATESI_v[self.Snnodos.index(vecino)]+=self.gammasn2
                            self.r6+=self.gammasn2  
                    
                    

                elif event == "r2":
                    if self.V==0:
                        self.r2=0 
                        continue
                    self.V -= 1
                    self.I_v += 1
                    indice=self.VRATESI.index(max(self.VRATESI))
                    eleccion=self.Vnodos[indice]                    
                    self.Vnodos.remove(eleccion)
                    self.I_vnodos.append(eleccion)
                    self.r1-=self.VRATESI_v[indice]
                    self.r2-=self.VRATESI[indice]
                    self.VRATESI_v.remove(self.VRATESI_v[indice])
                    self.VRATESI.remove(self.VRATESI[indice])
                    self.r11+=self.nuv

                    vecinos=list(self.graph1.neighbors(eleccion))           
                    
                    for vecino in vecinos:
                        if vecino in self.Vnodos:
                            self.VRATESI_v[self.Vnodos.index(vecino)]+=self.gammav1 
                            self.r1+=self.gammav1                    
                        elif vecino in self.Snodos:
                            self.SRATESI_v[self.Snodos.index(vecino)]+=self.gammas2
                            self.r4+=self.gammas2
                        elif vecino in self.Snnodos:
                            self.SnRATESI_v[self.Snnodos.index(vecino)]+=self.gammasn2
                            self.r6+=self.gammasn2
                    


                elif event == "r3":
                    if self.S==0:
                        self.r3=0 
                        continue
                    self.S -= 1
                    self.I += 1
                    if len(self.SRATESI)==0:
                        continue
                    indice=self.SRATESI.index(max(self.SRATESI))
                    eleccion=self.Snodos[indice]                   
                    self.Snodos.remove(eleccion)
                    self.Inodos.append(eleccion)
                    self.r4-=self.SRATESI_v[indice]
                    self.r3-=self.SRATESI[indice]
                    self.r8-=self.SRATESSn[indice]
                    self.SRATESI.remove(self.SRATESI[indice])
                    self.SRATESI_v.remove(self.SRATESI_v[indice])
                    self.SRATESSn.remove(self.SRATESSn[indice])
                    self.r10+=self.nu
                    #self.r7-=self.alfa

                    vecinos=list(self.graph1.neighbors(eleccion))           
                    
                    for vecino in vecinos:
                        if vecino in self.Vnodos:
                            self.VRATESI[self.Vnodos.index(vecino)]+=self.gammav2
                            self.r2+=self.gammav2                    
                        elif vecino in self.Snodos:
                            self.SRATESI[self.Snodos.index(vecino)]+=self.gammas1
                            self.r3+=self.gammas1
                        elif vecino in self.Snnodos:
                            self.SnRATESI[self.Snnodos.index(vecino)]+=self.gammasn1
                            self.r5+=self.gammasn1
                    


                elif event == "r4":
                    if self.S==0:
                        self.r4=0 
                        continue
                    self.S -= 1
                    self.I += 1       
                    indice=self.SRATESI_v.index(max(self.SRATESI_v))
                    eleccion=self.Snodos[indice]                     
                    self.Snodos.remove(eleccion)
                    self.Inodos.append(eleccion)
                    self.r4-=self.SRATESI_v[indice]
                    self.r3-=self.SRATESI[indice]
                    self.r8-=self.SRATESSn[indice]
                    self.SRATESI.remove(self.SRATESI[indice])
                    self.SRATESI_v.remove(self.SRATESI_v[indice])
                    self.SRATESSn.remove(self.SRATESSn[indice])
                    self.r10+=self.nu
                    #self.r7-=self.alfa

                    vecinos=list(self.graph1.neighbors(eleccion))           
                    
                    for vecino in vecinos:
                        if vecino in self.Vnodos:
                            self.VRATESI[self.Vnodos.index(vecino)]+=self.gammav2
                            self.r2+=self.gammav2                    
                        elif vecino in self.Snodos:
                            self.SRATESI[self.Snodos.index(vecino)]+=self.gammas1
                            self.r3+=self.gammas1
                        elif vecino in self.Snnodos:
                            self.SnRATESI[self.Snnodos.index(vecino)]+=self.gammasn1
                            self.r5+=self.gammasn1
                    

                elif event == "r5":
                    if self.Sn==0:
                        self.r5=0 
                        continue
                    self.Sn -= 1
                    self.I += 1      
                    #if self.r6==0:
                        #a=4
                    indice=self.SnRATESI.index(max(self.SnRATESI))
                    eleccion=self.Snnodos[indice]                    
                    self.Snnodos.remove(eleccion)
                    self.Inodos.append(eleccion)
                    self.r6-=self.SnRATESI_v[indice]
                    self.r5-=self.SnRATESI[indice]
                    self.r9-=self.SnRATESS[indice]
                    self.SnRATESI.remove(self.SnRATESI[indice])
                    self.SnRATESI_v.remove(self.SnRATESI_v[indice])
                    self.SnRATESS.remove(self.SnRATESS[indice])
                    self.r10+=self.nu
                    vecinos=list(self.graph1.neighbors(eleccion))           
                    
                    for vecino in vecinos:
                        if vecino in self.Vnodos:
                            self.VRATESI[self.Vnodos.index(vecino)]+=self.gammav2
                            self.r2+=self.gammav2                    
                        elif vecino in self.Snodos:
                            self.SRATESI[self.Snodos.index(vecino)]+=self.gammas1
                            self.r3+=self.gammas1
                        elif vecino in self.Snnodos:
                            self.SnRATESI[self.Snnodos.index(vecino)]+=self.gammasn1
                            self.r5+=self.gammasn1
                    



                elif event == "r6":
                    if self.Sn==0:
                        self.r6=0 
                        continue
                    self.Sn -= 1
                    self.I += 1    
                    indice=self.SnRATESI_v.index(max(self.SnRATESI_v))
                    eleccion=self.Snnodos[indice]  
                    self.Snnodos.remove(eleccion)
                    self.Inodos.append(eleccion)
                    self.r6-=self.SnRATESI_v[indice]
                    self.r5-=self.SnRATESI[indice]
                    self.r9-=self.SnRATESS[indice]
                    self.SnRATESI.remove(self.SnRATESI[indice])
                    self.SnRATESI_v.remove(self.SnRATESI_v[indice])
                    self.SnRATESS.remove(self.SnRATESS[indice])
                    self.r10+=self.nu
                    vecinos=list(self.graph1.neighbors(eleccion))           
                    
                    for vecino in vecinos:
                        if vecino in self.Vnodos:
                            self.VRATESI[self.Vnodos.index(vecino)]+=self.gammav2
                            self.r2+=self.gammav2                    
                        elif vecino in self.Snodos:
                            self.SRATESI[self.Snodos.index(vecino)]+=self.gammas1
                            self.r3+=self.gammas1
                        elif vecino in self.Snnodos:
                            self.SnRATESI[self.Snnodos.index(vecino)]+=self.gammasn1
                            self.r5+=self.gammasn1
                    



                
                    




                
                elif event == "r10":
                    if self.I==0:
                        self.r10=0 
                        continue
                    self.I -= 1
                    self.R += 1
                    eleccion=random.choice(self.Inodos)                    
                    self.Inodos.remove(eleccion)
                    self.Rnodos.append(eleccion)
                    vecinos=list(self.graph1.neighbors(eleccion))           
                    self.r10-=self.nu
                    for vecino in vecinos:
                        if vecino in self.Vnodos:
                            self.VRATESI[self.Vnodos.index(vecino)]-=self.gammav2
                            self.r2-=self.gammav2                    
                        elif vecino in self.Snodos:
                            self.SRATESI[self.Snodos.index(vecino)]-=self.gammas1
                            self.r3-=self.gammas1
                        elif vecino in self.Snnodos:
                            self.SnRATESI[self.Snnodos.index(vecino)]-=self.gammasn1
                            self.r5-=self.gammasn1
                    

                else:
                    if self.I_v==0:
                        self.r11=0 
                        continue
                    self.I_v -= 1
                    self.R += 1    
                    eleccion=random.choice(self.I_vnodos)                    
                    self.I_vnodos.remove(eleccion)
                    self.Rnodos.append(eleccion)
                    self.r11-=self.nuv
                    vecinos=list(self.graph1.neighbors(eleccion))           
                    
                    for vecino in vecinos:
                        if vecino in self.Vnodos:
                            self.VRATESI_v[self.Vnodos.index(vecino)]-=self.gammav1 
                            self.r1-=self.gammav1                    
                        elif vecino in self.Snodos:
                            self.SRATESI_v[self.Snodos.index(vecino)]-=self.gammas2
                            self.r4-=self.gammas2
                        elif vecino in self.Snnodos:
                            self.SnRATESI_v[self.Snnodos.index(vecino)]-=self.gammasn2
                            self.r6-=self.gammasn2
                    
                    



                #r8,r9=self.rates2()
                tr2 =self.r8+self.r9
                # Elegir aleatoriamente el tipo de evento que ocurre
                if tr2!=0 and self.r8>0 and self.r9>0:
                    event2 = np.random.choice(["r8","r9"], p=[self.r8/tr2,self.r9/tr2])
              
                    if event2 == "r8" :
                        if self.S==0:
                            self.r8=0 
                            continue
                        self.S -= 1
                        self.Sn += 1
                        indice=self.SRATESSn.index(max(self.SRATESSn))
                        eleccion=self.Snodos[indice]                        
                        self.Snodos.remove(eleccion)
                        self.Snnodos.append(eleccion)
                        self.r4-=self.SRATESI_v[indice]
                        self.r3-=self.SRATESI[indice]
                        self.r8-=self.SRATESSn[indice]
                        self.SRATESI.remove(self.SRATESI[indice])
                        self.SRATESI_v.remove(self.SRATESI_v[indice])
                        self.SRATESSn.remove(self.SRATESSn[indice])
                        #self.r7-=self.alfa
                       
                        vecinos=list(self.graph1.neighbors(eleccion))           
                        SnRATESI=SnRATESI_v=SnRATESS=0
                        for vecino in vecinos:
                            if vecino in self.Inodos:
                                SnRATESI+=self.gammasn1 
                                self.r5+=self.gammasn1                   
                            elif vecino in self.I_vnodos:
                                SnRATESI_v+=self.gammasn2
                                self.r6+=self.gammasn2
                        vecinos=list(self.graph2.neighbors(eleccion)) 
                        for vecino in vecinos:
                            if vecino in self.Snodos:
                                SnRATESS+=self.sigma
                                self.r9+=self.sigma
                        self.SnRATESI.append(SnRATESI)
                        self.SnRATESI_v.append(SnRATESI_v)
                        self.SnRATESS.append(SnRATESS)
                        
                        

                    else :
                        if self.Sn==0:
                            self.r9=0 
                            continue
                        self.Sn -= 1
                        self.S += 1    
                        indice=self.SnRATESS.index(max(self.SnRATESS))    
                        eleccion=self.Snnodos[indice]                   
                        self.Snnodos.remove(eleccion)
                        self.Snodos.append(eleccion)
                        self.r6-=self.SnRATESI_v[indice]
                        self.r5-=self.SnRATESI[indice]
                        self.r9-=self.SnRATESS[indice]   
                        self.SnRATESI.remove(self.SnRATESI[indice])
                        self.SnRATESI_v.remove(self.SnRATESI_v[indice]) 
                        self.SnRATESS.remove(self.SnRATESS[indice])
                        #self.r7+=self.alfa
                                            
                        vecinos=list(self.graph1.neighbors(eleccion))           
                        SRATESI=SRATESI_v=SRATESSn=0
                        for vecino in vecinos:
                            if vecino in self.Inodos:
                                SRATESI+=self.gammas1 
                                self.r3+=self.gammas1                   
                            elif vecino in self.I_vnodos:
                                SRATESI_v+=self.gammas2
                                self.r4+=self.gammas2
                        vecinos=list(self.graph2.neighbors(eleccion)) 
                        for vecino in vecinos:
                            if vecino in self.Snnodos:
                                SRATESSn+=self.beta
                                self.r8+=self.beta
                        self.SRATESI.append(SRATESI)
                        self.SRATESI_v.append(SRATESI_v)
                        self.SRATESSn.append(SRATESSn)
                        



                muerte=np.random.choice(['muere','nada'],p=[self.vitality,1-self.vitality])
                vacunación=np.random.choice(['vacuna','nada'],p=[self.alfa*(self.I+self.I_v)/self.N,1-self.alfa*(self.I+self.I_v)/self.N])
                if muerte=='muere' and self.R!=0 and (self.S!=0 or self.Sn!=0):
                    grupo=np.random.choice(['s','sn'],p=[self.S/(self.S+self.Sn),self.Sn/(self.S+self.Sn)])
                    if grupo=='s':
                        self.R-=1
                        self.S+=1
                        self.r11-=self.nuv
                        eleccion=random.choice(self.Rnodos)  
                        indice=self.Rnodos.index(eleccion)                  
                        self.Rnodos.remove(eleccion)
                        self.Snodos.append(eleccion)
                        vecinos=list(self.graph1.neighbors(eleccion))           
                        SRATESI=SRATESI_v=SRATESSn=0
                        for vecino in vecinos:
                            if vecino in self.Inodos:
                                SRATESI+=self.gammas1 
                                self.r3+=self.gammas1                   
                            elif vecino in self.I_vnodos:
                                SRATESI_v+=self.gammas2
                                self.r4+=self.gammas2
                        vecinos=list(self.graph2.neighbors(eleccion)) 
                        for vecino in vecinos:
                            if vecino in self.Snnodos:
                                SRATESSn+=self.beta
                                self.r8+=self.beta
                        self.SRATESI.append(SRATESI)
                        self.SRATESI_v.append(SRATESI_v)
                        self.SRATESSn.append(SRATESSn)
                    else :
                        self.R-=1
                        self.Sn+=1
                        self.r11-=self.nuv
                        eleccion=random.choice(self.Rnodos)  
                        indice=self.Rnodos.index(eleccion)                  
                        self.Rnodos.remove(eleccion)
                        self.Snnodos.append(eleccion)
                        vecinos=list(self.graph1.neighbors(eleccion))           
                        SnRATESI=SnRATESI_v=SnRATESS=0
                        for vecino in vecinos:
                            if vecino in self.Inodos:
                                SnRATESI+=self.gammasn1 
                                self.r5+=self.gammasn1                   
                            elif vecino in self.I_vnodos:
                                SnRATESI_v+=self.gammasn2
                                self.r6+=self.gammasn2
                        vecinos=list(self.graph2.neighbors(eleccion)) 
                        for vecino in vecinos:
                            if vecino in self.Snodos:
                                SnRATESS+=self.sigma
                                self.r9+=self.sigma
                        self.SnRATESI.append(SnRATESI)
                        self.SnRATESI_v.append(SnRATESI_v)
                        self.SnRATESS.append(SnRATESS)
                if vacunación=='vacuna'and self.S!=0 and self.t>self.tiempovacuna:
                    if self.Snodos==[]:
                        continue
                    self.S -= 1
                    self.V += 1
                    eleccion=random.choice(self.Snodos)  
                    indice=self.Snodos.index(eleccion)                  
                    self.Snodos.remove(eleccion)
                    self.Vnodos.append(eleccion)
                    self.r4-=self.SRATESI_v[indice]
                    self.r3-=self.SRATESI[indice]
                    self.r8-=self.SRATESSn[indice]
                    self.SRATESI.remove(self.SRATESI[indice])
                    self.SRATESI_v.remove(self.SRATESI_v[indice])
                    self.SRATESSn.remove(self.SRATESSn[indice])
                
                    vecinos=list(self.graph1.neighbors(eleccion)) 
                    if len(self.Vnodos)!=len(self.VRATESI)!=len(self.VRATESI_v) and self.I!=len(self.Inodos):
                        self.r1,self.r2,self.r3,self.r4,self.r5,self.r6,self.r10,self.r11=self.rates1()
                        self.r8,self.r9=self.rates2()          
                    VRATESI=VRATESI_v=0
                    for vecino in vecinos:
                        if vecino in self.Inodos:                                
                            VRATESI+=self.gammav2 
                            self.r2+=self.gammav2                   
                        elif vecino in self.I_vnodos:
                            VRATESI_v+=self.gammav1
                            self.r1+=self.gammav1
                    self.VRATESI.append(VRATESI)
                    self.VRATESI_v.append(VRATESI_v)
                
                        
                        


                self.t += delta_t
                #print(self.t)

                # Almacenar los resultados
                self.time_list.append(self.t)
                self.S_list.append(self.S)
                self.Sn_list.append(self.Sn)
                self.V_list.append(self.V)
                self.I_list.append(self.I)
                self.I_v_list.append(self.I_v)
                self.R_list.append(self.R)






    def Graficar1(self):
        # Graficar los resultados
        plt.clf()
        #sumo las listas 
        Stlist = [x + y for x, y in zip(self.S_list,self.Sn_list)]
        ItList = [x + y for x, y in zip(self.I_list,self.I_v_list)]
        plt.plot(self.time_list, Stlist , label="Susceptibles")
       
        plt.plot(self.time_list, ItList, label="Infectados")        
        plt.plot(self.time_list, self.R_list, label="Recuperados")
        plt.plot(self.time_list, self.V_list, label="Vacunados sanos", color='c')
        #plt.plot(time_list, R_list, label="Recuperados")
        plt.xlabel("Tiempo")
        plt.ylabel("Número de individuos")
        #texto="Figura_{0}_{1}_\n{2}_{3}_{4}\n_{5}_{6}_{7}\n_{8}_{9}_\n{10}.png".format(self.gammav1,self.gammav2,self.gammas1,self.gammas2,self.gammasn1,self.gammasn2,self.alfa,self.beta,self.sigma,self.nu,self.nuv)
        #plt.text(4.5, 9, texto, ha='right',va='top')
        plt.legend()
        # Crear la carpeta donde se va aguardar si no existe
        if not os.path.exists("Imagenes"):
            os.makedirs("Imagenes")
        if not os.path.exists(os.path.join("Imagenes", "PROTOTIPO3mv")):
            os.makedirs(os.path.join("Imagenes", "PROTOTIPO3mv"))
        if not os.path.exists(os.path.join("Imagenes", "PROTOTIPO3mv", "{0}_{1}_{2}_{3}_{4}".format(self.alfa,self.beta,self.sigma,self.tiempovacuna,self.vitality))):
            os.makedirs(os.path.join("Imagenes", "PROTOTIPO3mv", "{0}_{1}_{2}_{3}_{4}".format(self.alfa,self.beta,self.sigma,self.tiempovacuna,self.vitality)))

        # Guardar la figura en la carpeta "imagenes" dentro de "proyecto"
        filepath = os.path.join("Imagenes", "PROTOTIPO3mv", "{0}_{1}_{2}_{3}_{4}".format(self.alfa,self.beta,self.sigma,self.tiempovacuna,self.vitality),"resumen.png")
        plt.savefig(filepath)
        #print('Simulacion1 realizada.')
        


    def Graficar2(self):
        # Graficar los resultados
        plt.clf()
        #sumo las listas 
        
        
        plt.plot(self.time_list, self.S_list , label="Susceptibles provacunas")        
        plt.plot(self.time_list, self.I_v_list, label="Infectados vacunados")
        plt.plot(self.time_list, self.R_list, label="Recuperados")
        plt.plot(self.time_list, self.I_list, label="Infectados no vacunados",color='r')       
        
        plt.plot(self.time_list, self.V_list, label="Vacunados sanos", color='c')
        plt.plot(self.time_list, self.Sn_list , label="Susceptibles antivacunas")
        #plt.plot(time_list, R_list, label="Recuperados")
        plt.xlabel("Tiempo")
        plt.ylabel("Número de individuos")
        #texto="Figura_{0}_{1}_\n{2}_{3}_{4}\n_{5}_{6}_{7}\n_{8}_{9}_\n{10}.png".format(self.gammav1,self.gammav2,self.gammas1,self.gammas2,self.gammasn1,self.gammasn2,self.alfa,self.beta,self.sigma,self.nu,self.nuv)
        #plt.text(4.5, 9, texto, ha='right',va='top')
        plt.legend()
        # Crear la carpeta donde se va aguardar si no existe
        if not os.path.exists("Imagenes"):
            os.makedirs("Imagenes")
        if not os.path.exists(os.path.join("Imagenes", "PROTOTIPO3mv")):
            os.makedirs(os.path.join("Imagenes", "PROTOTIPO3mv"))
        if not os.path.exists(os.path.join("Imagenes", "PROTOTIPO3mv", "{0}_{1}_{2}_{3}_{4}".format(self.alfa,self.beta,self.sigma,self.tiempovacuna,self.vitality))):
            os.makedirs(os.path.join("Imagenes", "PROTOTIPO3mv", "{0}_{1}_{2}_{3}_{4}".format(self.alfa,self.beta,self.sigma,self.tiempovacuna,self.vitality)))

        # Guardar la figura en la carpeta "imagenes" dentro de "proyecto"
        filepath = os.path.join("Imagenes", "PROTOTIPO3mv", "{0}_{1}_{2}_{3}_{4}".format(self.alfa,self.beta,self.sigma,self.tiempovacuna,self.vitality),"todos.png")
        plt.savefig(filepath)
        #print('Simulacion2 realizada.')




    def Fichero(self):
        if not os.path.exists("Imagenes"):
            os.makedirs("Imagenes")
        if not os.path.exists(os.path.join("Imagenes", "PROTOTIPO3mv")):
            os.makedirs(os.path.join("Imagenes", "PROTOTIPO3mv"))
        if not os.path.exists(os.path.join("Imagenes", "PROTOTIPO3mv", "{0}_{1}_{2}_{3}_{4}".format(self.alfa,self.beta,self.sigma,self.tiempovacuna,self.vitality))):
            os.makedirs(os.path.join("Imagenes", "PROTOTIPO3mv", "{0}_{1}_{2}_{3}_{4}".format(self.alfa,self.beta,self.sigma,self.tiempovacuna,self.vitality)))

        # Nombre del archivo
        nombre_archivo = os.path.join("Imagenes", "PROTOTIPO3mv", "{0}_{1}_{2}_{3}_{4}".format(self.alfa,self.beta,self.sigma,self.tiempovacuna,self.vitality), 'datos.txt')

        # Obtiene la longitud máxima de las listas
        longitud_maxima = max(len(self.time_list), len(self.S_list), len(self.Sn_list), len(self.V_list), len(self.I_list),len(self.I_v_list), len(self.R_list))

        # Abre el archivo en modo escritura
        with open(nombre_archivo, 'w') as archivo:
            # Escribe los elementos de cada lista en columnas correspondientes
            for i in range(longitud_maxima):
                if i < len(self.time_list):
                    archivo.write(str(self.time_list[i]) + '\t')
                else:
                    archivo.write('\t')
                
                if i < len(self.S_list):
                    archivo.write(str(self.S_list[i]) + '\t')
                else:
                    archivo.write('\t')
                
                if i < len(self.Sn_list):
                    archivo.write(str(self.Sn_list[i]) + '\t')
                else:
                    archivo.write('\t')
                
                if i < len(self.V_list):
                    archivo.write(str(self.V_list[i]) + '\t')
                else:
                    archivo.write('\t')
                
                if i < len(self.I_list):
                    archivo.write(str(self.I_list[i]) + '\t')
                else:
                    archivo.write('\t')
                
                if i < len(self.I_v_list):
                    archivo.write(str(self.I_v_list[i]) + '\t')
                else:
                    archivo.write('\t')
                
                if i < len(self.V_list):
                    archivo.write(str(self.R_list[i]) + '\t')
                else:
                    archivo.write('\t')
                archivo.write('\n')
    def area(self):

        if not os.path.exists("Imagenes"):
            os.makedirs("Imagenes")
        if not os.path.exists(os.path.join("Imagenes", "PROTOTIPO3mv")):
            os.makedirs(os.path.join("Imagenes", "PROTOTIPO3mv"))
        if not os.path.join("Imagenes", "PROTOTIPO3mv", "{0}_{1}_{2}_{3}_{4}".format(self.alfa,self.beta,self.sigma,self.tiempovacuna,self.vitality)):
            os.path.join("Imagenes", "PROTOTIPO3mv", "{0}_{1}_{2}_{3}_{4}".format(self.alfa,self.beta,self.sigma,self.tiempovacuna,self.vitality))

        # Nombre del archivo
        nombre_archivo = os.path.join("Imagenes", "PROTOTIPO3mv", "{0}_{1}_{2}_{3}_{4}".format(self.alfa,self.beta,self.sigma,self.tiempovacuna,self.vitality), 'area.txt')

        # Aplica un filtro de media móvil para suavizar la curva
        window_size = 15  # Tamaño de la ventana para el filtro de media móvil
        I_suavizado = np.convolve(self.I_list, np.ones(window_size) / window_size, mode='same')
        I_v_suavizado = np.convolve(self.I_v_list, np.ones(window_size) / window_size, mode='same')

        # Encuentra los puntos de inflexión en la curva suavizada
        puntos_inflexion1 = argrelextrema(I_suavizado, np.less)[0]
        puntos_inflexion2 = argrelextrema(I_v_suavizado, np.less)[0]

        # Obtén los índices mínimo y máximo de los puntos de inflexión
        if puntos_inflexion1!=[]:
            limite1 = np.max(puntos_inflexion1)
        if puntos_inflexion2!=[]:            
            limite2 = np.max(puntos_inflexion2)
            
        with open(nombre_archivo, 'w') as archivo:
            # Escribe los elementos de cada lista en columnas correspondientes
            if puntos_inflexion1!=[]:        
                archivo.write('Limite:\t'+str(self.time_list[limite1])+'\n')
                area1=trapz(self.I_list[:limite1],self.time_list[:limite1])
                archivo.write('Area I: \t'+ str(area1) + '\n')
            else:
                area1=0
            if puntos_inflexion2!=[]:         
                archivo.write('Limite:\t'+str(self.time_list[limite2])+'\n')
                area2=trapz(self.I_v_list[:limite2],self.time_list[:limite2])
                archivo.write('Area I_v: \t'+ str(area2) + '\n')
            else:
                area2=0
            areat=area1+area2
            archivo.write('Area It: \t'+ str(areat) + '\n')
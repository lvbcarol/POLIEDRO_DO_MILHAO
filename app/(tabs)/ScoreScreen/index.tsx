/*import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet, Image, Dimensions, ImageBackground } from 'react-native';
import { useRouter } from 'expo-router';

const PontuacaoScreen: React.FC = () => {
  const router = useRouter();

  const handleReturnHome = () => {
    router.push('../../../(tabs)/HomeScreen/'); 
  };

  return (
    <ImageBackground
      source={require('../../../assets/images/TelaVermelha.png')}
      style={styles.image}
      resizeMode="cover"
    >
        <View style={styles.bullets}>
                  {Array.from({ length: 30}).map((_, index) => (
                    <View key={index} style={styles.bullet} />
                  ))}
                </View>
      <View style={styles.container}>
        <Text style={styles.title}>POLIEDRO DO MILHÃO</Text>

        <View style={styles.moneyRain}>
          <Text style={styles.congratsText}>PARABÉNS!{'\n'}VOCÊ GANHOU</Text>
          <Text style={styles.amount}>R$1.000.000,00</Text>
        </View>

        <TouchableOpacity style={styles.arrowButton} onPress={handleReturnHome}>
          <Text style={styles.arrow}>➜</Text>
        </TouchableOpacity>
      </View>
      <View style={styles.bullets}>
                {Array.from({ length: 50 }).map((_, index) => (
                  <View key={index} style={styles.bullet} />
                ))}
              </View>
    </ImageBackground>
  );
};

const { width } = Dimensions.get('window');

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
    backgroundColor: 'rgba(0, 0, 0, 0.4)',
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#FFD700',
    marginBottom: 30,
    textAlign: 'center',
  },
  moneyRain: {
    backgroundColor: '#790000',
    borderRadius: 16,
    padding: 30,
    alignItems: 'center',
    marginBottom: 40,
  },
  congratsText: {
    color: 'white',
    fontSize: 22,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 10,
  },
  amount: {
    color: '#FFD700',
    fontSize: 26,
    fontWeight: 'bold',
  },
  arrowButton: {
    backgroundColor: '#FFD700',
    borderRadius: 50,
    padding: 10,
    width: 60,
    height: 60,
    alignItems: 'center',
    justifyContent: 'center',
    position: 'absolute',
    right: 30,
    bottom: 30,
  },
  arrow: {
    fontSize: 28,
    color: 'black',
    fontWeight: 'bold',
  },
  image: {
    flex: 1,
    width: 'auto',
    height: 'auto',
  },
  bullets: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'center',
    marginVertical: 8,
  },
  bullet: {
    width: 10,
    height: 10,
    borderRadius: 5,
    backgroundColor: 'gold',
    margin: 3,
  },
});

export default PontuacaoScreen;*/

/*comentei a tela que vcs tinham feito e substitui por essa que está com as rotas do back, 
mas se não rodar pode voltar para o original tirando estes comentários, mas acredito que esteja certo*/

import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { useRouter } from 'expo-router';

export default function ScoreScreen() {
  const router = useRouter();

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Fim de Jogo</Text>
      <Text style={styles.subtitle}>Obrigado por jogar!</Text>
      <TouchableOpacity style={styles.button} onPress={() => router.push('/')}>
        <Text style={styles.buttonText}>Voltar ao Início</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#002244',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 24,
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#FFD700',
    marginBottom: 16,
  },
  subtitle: {
    fontSize: 20,
    color: '#FFF',
    marginBottom: 32,
  },
  button: {
    backgroundColor: '#FFD700',
    paddingVertical: 12,
    paddingHorizontal: 24,
    borderRadius: 8,
  },
  buttonText: {
    color: '#002244',
    fontSize: 18,
    fontWeight: 'bold',
  },
});

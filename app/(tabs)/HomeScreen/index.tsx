import { Image } from 'react-native';
import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet, Dimensions, ImageBackground } from 'react-native';
import { useRouter } from 'expo-router';

const { width } = Dimensions.get('window');

const StartScreen: React.FC = () => {
  const router = useRouter();

  const handleStart = () => {
    router.push('../../../(tabs)/SerieScreen');
  };

  const handleHistory = () => {
    router.push('../../../(tabs)/HistoricoScreen');
  };

  return (
    <ImageBackground
      source={require('../../../assets/images/TelaAzul.png')} 
      style={styles.background}
      resizeMode="cover"
    >
      <View style={styles.overlay}>
        <Text style={styles.title}>POLIEDRO{"\n"}DO MILHÃO</Text>
            <Image source={require('../../../assets/images/Coin.png')} style={styles.coin} />  
                
            <Image source={require('../../../assets/images/Cortina1.png')} style={styles.Image}/>

        <TouchableOpacity style={styles.button} onPress={handleStart}>
          <Text style={styles.buttonText}>Jogar</Text>
        </TouchableOpacity>

        <TouchableOpacity style={styles.button} onPress={handleHistory}>
          <Text style={styles.buttonText}>Histórico</Text>
        </TouchableOpacity>
      </View>
    </ImageBackground>
  );
};

const styles = StyleSheet.create({
  background: {
    flex: 1,
    width: '100%',
    height: '100%',
  },
  overlay: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    paddingHorizontal: 30,
    backgroundColor: 'rgba(0, 0, 0, 0.4)', // leve escurecimento para contraste
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#FFD700',
    marginBottom: 15,
    textAlign: 'center',
  },
  subtitle: {
    fontSize: 18,
    color: '#fff',
    marginBottom: 40,
    textAlign: 'center',
  },
  button: {
    backgroundColor: '#d5241c',
    paddingVertical: 15,
    paddingHorizontal: 50,
    borderRadius: 30,
    marginBottom: 20,
    width: '25%',
    alignItems: 'center',
  },
  buttonText: {
    color: '#ffffff',
    fontWeight: 'bold',
  },
  coin: {
    width: 80,
    height: 80,
    marginBottom: 30,
  },
  Image: {
      position: 'absolute',
      top: '0%',
      transform: [{ translateY: -40 }], // centraliza verticalmente (ajuste o valor)
      width: 1550,
      height: 800,
    },
});

export default StartScreen;

import { Dimensions } from 'react-native';
const { width, height } = Dimensions.get('window');
import { useRouter } from 'expo-router';
import { StatusBar } from 'expo-status-bar';
import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, ImageBackground, Image } from 'react-native';

export default function App() {
  const router = useRouter();
  const [nickname, setNickname] = useState('');
  const [senha, setSenha] = useState('');

  const handleCadastro = () => {
    // Aqui você pode colocar a lógica de cadastro
    console.log('Nickname:', nickname);
    console.log('Senha:', senha);
    router.push('../(tabs)/HomeScreen/');
  };

  return (
    <ImageBackground
      source={require('../../assets/images/TelaAzul.png')} 
      style={styles.container}
      resizeMode="cover"
    >
      <View style={styles.overlay}>
        <Text style={styles.title}>POLIEDRO{"\n"}DO MILHÃO</Text>
        <Image source={require('../../assets/images/Coin.png')} style={styles.coin} />  
        
        <Image source={require('../../assets/images/Cortina1.png')} style={styles.Image}/>

        <TextInput
          style={styles.input}
          placeholder="Nickname:"
          placeholderTextColor="#fff"
          onChangeText={setNickname}
          value={nickname}
        />
        <TextInput
          style={styles.input}
          placeholder="Senha:"
          placeholderTextColor="#fff"
          secureTextEntry
          onChangeText={setSenha}
          value={senha}
        />
        <TouchableOpacity style={styles.button} onPress={handleCadastro}>
          <Text style={styles.buttonText}>Entrar</Text>
        </TouchableOpacity>
      </View>
    </ImageBackground>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    width: 'auto',
    height: 'auto',
  },
  overlay: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    paddingHorizontal: 20,
    backgroundColor: 'rgba(0, 0, 0, 0.4)', // leve escurecimento para contraste
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    textAlign: 'center',
    color: '#FFD700',
    marginBottom: 10,
  },
  coin: {
    width: 80,
    height: 80,
    marginBottom: 30,
  },
  input: {
    backgroundColor: '#d5241c',
    width: '25%',
    padding: 12,
    borderRadius: 25,
    marginVertical: 8,
    color: 'white',
    textAlign: 'center',
    fontWeight: 'bold',
  },
  button: {
    backgroundColor: 'transparent',
    paddingVertical: 12,
    paddingHorizontal: 30,
    borderRadius: 20,
    marginTop: 10,
  },
  buttonText: {
    color: 'white',
    fontWeight: 'bold',
  },
  Image: {
    position: 'absolute',
    top: '0%',
    transform: [{ translateY: -40 }],
    width: 1550,
    height: 800,
    zIndex: -1, // <-- imagem vai para trás
  }
  ,
})
;
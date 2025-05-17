//import { Dimensions } from 'react-native';
//const { width, height } = Dimensions.get('window');
//import { StatusBar } from 'expo-status-bar';
import { useNavigation, useRouter } from 'expo-router';
import React, { useState } from 'react';
import {TextInput, TouchableOpacity, ImageBackground, Image, View, Text, StyleSheet, useWindowDimensions, ScrollView} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import axios from 'axios';

export default function App() {
  // navegação entre telas:
  const router = useRouter();
  // responsividade
  const { width } = useWindowDimensions();
  // cadastro
  const [nickname, setNickname] = useState('');
  const [senha, setSenha] = useState('');

  // função de login 
  const handleCadastro = async () => {
  if (!nickname || !senha) {
    alert('Preencha todos os campos!');
    return;
  }

  try {
    const response = await axios.post('http://192.168.15.1:5000/login', {
      nickname,
      senha
    });

    const { access_token, ID_usuario, nickname: nomeUsuario } = response.data;

    // Salve o token localmente para uso futuro (ex: rotas protegidas)
    // Pode usar AsyncStorage ou contexto global (Ex: Context API ou Redux)
    console.log('Token JWT:', access_token);

    // Navega para a tela principal
    router.push('../(tabs)/HomeScreen/');

  } catch (error: any) {
    if (error.response && error.response.status === 401) {
      alert('Nickname ou senha inválidos!');
    } else {
      alert('Erro ao fazer login. Tente novamente.');
      console.error(error);
    }
  }
};

  //vai para a tela de cadastro de usuário
  const handleIrParaCadastro = () => {
    router.push('../../(tabs)/CadastroScreen/'); 
  };
  

  return (
    <ScrollView contentContainerStyle={styles.scroll}>
      {/* imagem de fundo */}
      <ImageBackground
        source={require('../../assets/images/TelaAzul.png')} 
        style={styles.container}
        resizeMode="cover"
      > 
        {/* Ícone de som */}
        <TouchableOpacity style={[styles.soundIcon, width > 768 && styles.soundIconDesktop]}>
          <Ionicons name="volume-high" size={30} color="white" />
        </TouchableOpacity>

        {/* largura maior que 768 ativa um estilo para 'desktop' */}
        <View style={[styles.overlay, width > 768 && styles.overlayDesktop]}>
          <Text style={[styles.title, width > 768 && styles.titleDesktop]}>POLIEDRO{"\n"}DO MILHÃO</Text>
          <Image source={require('../../assets/images/Coin.png')} style={styles.coin} />  
          
          {/* <Image source={require('../../assets/images/Cortina1.png')} style={styles.Image}/> */}

          <TextInput
            style={[styles.input, width > 768 ? styles.inputDesktop : null]}
            placeholder="Nickname:"
            placeholderTextColor="#fff"
            onChangeText={setNickname}
            value={nickname}
          />
          <TextInput
            style={[styles.input, width > 768 ? styles.inputDesktop : null]}
            placeholder="Senha:"
            placeholderTextColor="#fff"
            secureTextEntry 
            onChangeText={setSenha}
            value={senha}
          />

          <TouchableOpacity style={styles.button} onPress={handleCadastro}>
            <Text style={styles.buttonText}>Entrar</Text>
          </TouchableOpacity>
          
          <View style={styles.row}>
          <Text style={styles.text}>Ainda não tem conta?</Text>
          <TouchableOpacity style={styles.button1} onPress={handleIrParaCadastro}>
            <Text style={styles.buttonText1}>Cadastre-se</Text>
          </TouchableOpacity>
          </View>

        </View>
      </ImageBackground>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  // imagem de fundo 
  container: {
    flex: 1,
    width: '100%',
    height: '100%',
  },
  // garante que o conteúdo cresça para ocupar o espaço inteiro da tela
  scroll: {
    flexGrow: 1,
  },
  // sobre o fundo azul, centralizando todos os elementos no centro
  overlay: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    paddingHorizontal: 20,
    backgroundColor: 'rgba(0, 0, 0, 0.4)', 
  },
  // para telas grandes
  overlayDesktop: {
    paddingHorizontal: 80,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    textAlign: 'center',
    color: '#FFD700',
    marginBottom: 10,
  },
  // para telas grandes
  titleDesktop: {
    fontSize: 40,
  },
  coin: {
    width: 80,
    height: 80,
    marginBottom: 30,
  },
  input: {
    backgroundColor: '#d5241c',
    width: '70%',
    padding: 12,
    borderRadius: 25,
    marginVertical: 8,
    color: 'white',
    textAlign: 'center',
    fontWeight: 'bold',
  },
  //para telas grandes
  inputDesktop: {
    width: 400,
    fontSize: 18,
  },
  button: {
    backgroundColor: '#FFD700',
    paddingVertical: 12,
    paddingHorizontal: 30,
    borderRadius: 20,
    marginTop: 10,
  },
  buttonText: {
    color: '#7b1113',
    fontWeight: 'bold',
  },
  button1: {
    //backgroundColor: 'white',
    paddingVertical: 7,
    paddingHorizontal: 4,
    borderRadius: 20,
    marginTop: 2,
  },
  buttonText1: {
    color: '#999',
    fontWeight: 'bold',
    textDecorationLine: 'underline',
  },
  // Image: {
  //   position: 'absolute',
  //   top: 0,
  //   transform: [{ translateY: -40 }],
  //   width: '100%',
  //   height: undefined,
  //   aspectRatio: 3/2,
  //   resizeMode: 'cover',
  //   zIndex: -1, // <-- imagem vai para trás
  // },
  text: {
    color: '#999',
  },
  // link: {
  //   color: '#2da7c2',
  //   fontWeight: 'bold',
  //   paddingHorizontal: 6,
  //   paddingVertical: 2,
  //   borderWidth: 1,
  //   borderColor: '#c8e165',
  //   backgroundColor: '#f9ffea',
  //   borderRadius: 4,
  //   overflow: 'hidden',
  // },
  //  "Ainda não tem conta?" + botão "Cadastre-se"
  row: {
    flexDirection: 'row',
    alignItems: 'center',
    marginTop: 10,
    gap: 5, // Espaço entre os elementos
  },
  soundIcon: {
    position: 'absolute',
    top: 40,
    right: 30,
    zIndex: 5,
  },
  soundIconDesktop: {
    position: 'absolute',
    top: 40,
    right: 40,
    zIndex: 5,
  },
})
;
import { Dimensions } from 'react-native';
const { width, height } = Dimensions.get('window');
import { useRouter } from 'expo-router';
import React, { useState } from 'react';
import {
  TextInput,
  TouchableOpacity,
  ImageBackground,
  Image,
  View,
  Text,
  StyleSheet,
  useWindowDimensions,
  ScrollView,
} from 'react-native';

export default function CadastroScreen() {
  const router = useRouter();
  const { width } = useWindowDimensions();
  const [nomeCompleto, setNomeCompleto] = useState('');
  const [email, setEmail] = useState('');
  const [nickname, setNickname] = useState('');
  const [senha, setSenha] = useState('');

  const handleFinalizarCadastro = () => {
    // Aqui você pode implementar a lógica de salvar os dados do usuário
    console.log('Cadastro realizado com sucesso:');
    console.log({ nomeCompleto, email, nickname, senha });

    // Redireciona para a HomeScreen após o cadastro
    router.push('../(tabs)/HomeScreen/');
  };

  return (
    <ScrollView contentContainerStyle={styles.scroll}>
      <ImageBackground
        source={require('../../../assets/images/TelaAzul.png')}
        style={styles.container}
        resizeMode="cover"
      >
        <View style={[styles.overlay, width > 768 && styles.overlayDesktop]}>

          <Text style={[styles.title, width > 768 && styles.titleDesktop]}>POLIEDRO{"\n"}DO MILHÃO</Text>
          <Image source={require('../../../assets/images/Coin.png')} style={styles.coin} />
          
          <Text style={[styles.subtitle, width > 768 && styles.titleDesktop]}>CADASTRO USUÁRIO</Text>

          <TextInput
            style={[styles.input, width > 768 && styles.inputDesktop]}
            placeholder="Email"
            placeholderTextColor="#fff"
            onChangeText={setEmail}
            value={email}
          />
          <TextInput
            style={[styles.input, width > 768 && styles.inputDesktop]}
            placeholder="Nickname"
            placeholderTextColor="#fff"
            onChangeText={setNickname}
            value={nickname}
          />
          <TextInput
            style={[styles.input, width > 768 && styles.inputDesktop]}
            placeholder="Senha"
            placeholderTextColor="#fff"
            secureTextEntry
            onChangeText={setSenha}
            value={senha}
          />

          <TouchableOpacity style={styles.button} onPress={handleFinalizarCadastro}>
            <Text style={styles.buttonText}>Finalizar Cadastro</Text>
          </TouchableOpacity>
        </View>
      </ImageBackground>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    width: '100%',
    height: '100%',
  },
  scroll: {
    flexGrow: 1,
  },
  overlay: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    paddingHorizontal: 20,
    backgroundColor: 'rgba(0, 0, 0, 0.4)',
  },
  overlayDesktop: {
    paddingHorizontal: 80,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    textAlign: 'center',
    color: '#FFD700',
    marginBottom: 20,
  },
  titleDesktop: {
    fontSize: 40,
  },
  subtitle: {
    fontSize: 20,
    fontWeight: 'bold',
    textAlign: 'center',
    color: '#FFD700',
    marginBottom: 10,
  },
  input: {
    backgroundColor: '#d5241c',
    width: '80%',
    padding: 12,
    borderRadius: 25,
    marginVertical: 8,
    color: 'white',
    textAlign: 'center',
    fontWeight: 'bold',
  },
  inputDesktop: {
    width: 400,
    fontSize: 18,
  },
  button: {
    backgroundColor: '#FFD700',
    paddingVertical: 12,
    paddingHorizontal: 30,
    borderRadius: 25,
    marginTop: 20,
  },
  buttonText: {
    color: '#7b1113',
    fontWeight: 'bold',
    fontSize: 16,
  },
  coin: {
    width: 80,
    height: 80,
    marginBottom: 30,
  },
});
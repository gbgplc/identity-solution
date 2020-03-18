const webpackCommonConfig = {
	resolve: {
		extensions: ['.ts', '.tsx', '.js', '.json', 'scss'],
	},
	stats: {
		assets: true,
		chunks: false,
		entrypoints: false,
		excludeAssets: /\.d\.ts/,
		modules: false,
	},
};

module.exports = webpackCommonConfig;

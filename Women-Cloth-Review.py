{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPbwf1/ZULV2ak4LyGGMOZ5",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AVUKU-PRAGATHESWARI/women_cloth_review/blob/main/womencloth.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Title of Project :**\n",
        "**Women Cloth Reviews Prediction with Multi-Nomial Naive Bayes**"
      ],
      "metadata": {
        "id": "TjyjpC_HWHoD"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "\n",
        "---\n",
        "\n"
      ],
      "metadata": {
        "id": "iXuxjMHbWXX2"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Objectives:**\n",
        "**The objective of this project is to predict women's clothing reviews using a Multi-Nomial Naive Bayes model. The model aims to classify reviews based on their sentiment or other relevant criteria.**\n",
        "\n"
      ],
      "metadata": {
        "id": "t1AUJq_yY3sZ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Data Source:**\n",
        "**The dataset used for this project is sourced from [GitHub](https://github.com/YBIFoundation/ProjectHub-MachineLearning/raw/main/Women%20Clothing%20E-Commerce%20Review.csv).**"
      ],
      "metadata": {
        "id": "PfmMYhtUYDmx"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Import** **Library**"
      ],
      "metadata": {
        "id": "D_xQBFbAWZXr"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "CcFYvLrxN480"
      },
      "outputs": [],
      "source": [
        "import pandas as pd"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np"
      ],
      "metadata": {
        "id": "mZbetr9mObab"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt"
      ],
      "metadata": {
        "id": "p87fK1oeObbm"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import seaborn as sns"
      ],
      "metadata": {
        "id": "z3-LUdUVObgr"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Import Data**"
      ],
      "metadata": {
        "id": "vqgSzDllZ0YV"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_csv(\"https://github.com/YBIFoundation/ProjectHub-MachineLearning/raw/main/Women%20Clothing%20E-Commerce%20Review.csv\")"
      ],
      "metadata": {
        "id": "F2XzPttkObko"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Describe Data**"
      ],
      "metadata": {
        "id": "sF5r--yaZ7Uo"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 608
        },
        "id": "6i65JRtuOboK",
        "outputId": "9076c86f-6bf5-4a4a-a9ea-afb0df5dc49f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Clothing ID  Age                    Title  \\\n",
              "0          767   33                      NaN   \n",
              "1         1080   34                      NaN   \n",
              "2         1077   60  Some major design flaws   \n",
              "3         1049   50         My favorite buy!   \n",
              "4          847   47         Flattering shirt   \n",
              "\n",
              "                                              Review  Rating  Recommended  \\\n",
              "0  Absolutely wonderful - silky and sexy and comf...       4            1   \n",
              "1  Love this dress!  it's sooo pretty.  i happene...       5            1   \n",
              "2  I had such high hopes for this dress and reall...       3            0   \n",
              "3  I love, love, love this jumpsuit. it's fun, fl...       5            1   \n",
              "4  This shirt is very flattering to all due to th...       5            1   \n",
              "\n",
              "   Positive Feedback        Division Department   Category  \n",
              "0                  0       Initmates   Intimate  Intimates  \n",
              "1                  4         General    Dresses    Dresses  \n",
              "2                  0         General    Dresses    Dresses  \n",
              "3                  0  General Petite    Bottoms      Pants  \n",
              "4                  6         General       Tops    Blouses  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-f355ae20-486f-46b8-a554-0bce97393c6a\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Clothing ID</th>\n",
              "      <th>Age</th>\n",
              "      <th>Title</th>\n",
              "      <th>Review</th>\n",
              "      <th>Rating</th>\n",
              "      <th>Recommended</th>\n",
              "      <th>Positive Feedback</th>\n",
              "      <th>Division</th>\n",
              "      <th>Department</th>\n",
              "      <th>Category</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>767</td>\n",
              "      <td>33</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Absolutely wonderful - silky and sexy and comf...</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>Initmates</td>\n",
              "      <td>Intimate</td>\n",
              "      <td>Intimates</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1080</td>\n",
              "      <td>34</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Love this dress!  it's sooo pretty.  i happene...</td>\n",
              "      <td>5</td>\n",
              "      <td>1</td>\n",
              "      <td>4</td>\n",
              "      <td>General</td>\n",
              "      <td>Dresses</td>\n",
              "      <td>Dresses</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1077</td>\n",
              "      <td>60</td>\n",
              "      <td>Some major design flaws</td>\n",
              "      <td>I had such high hopes for this dress and reall...</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>General</td>\n",
              "      <td>Dresses</td>\n",
              "      <td>Dresses</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1049</td>\n",
              "      <td>50</td>\n",
              "      <td>My favorite buy!</td>\n",
              "      <td>I love, love, love this jumpsuit. it's fun, fl...</td>\n",
              "      <td>5</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>General Petite</td>\n",
              "      <td>Bottoms</td>\n",
              "      <td>Pants</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>847</td>\n",
              "      <td>47</td>\n",
              "      <td>Flattering shirt</td>\n",
              "      <td>This shirt is very flattering to all due to th...</td>\n",
              "      <td>5</td>\n",
              "      <td>1</td>\n",
              "      <td>6</td>\n",
              "      <td>General</td>\n",
              "      <td>Tops</td>\n",
              "      <td>Blouses</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-f355ae20-486f-46b8-a554-0bce97393c6a')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-f355ae20-486f-46b8-a554-0bce97393c6a button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-f355ae20-486f-46b8-a554-0bce97393c6a');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-c3666845-737b-451b-b9e7-801b4ebb42f9\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-c3666845-737b-451b-b9e7-801b4ebb42f9')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-c3666845-737b-451b-b9e7-801b4ebb42f9 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "69bytityObpo",
        "outputId": "275a12fb-d2b1-41af-93bf-dd5d66f4e5dd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 23486 entries, 0 to 23485\n",
            "Data columns (total 10 columns):\n",
            " #   Column             Non-Null Count  Dtype \n",
            "---  ------             --------------  ----- \n",
            " 0   Clothing ID        23486 non-null  int64 \n",
            " 1   Age                23486 non-null  int64 \n",
            " 2   Title              19676 non-null  object\n",
            " 3   Review             22641 non-null  object\n",
            " 4   Rating             23486 non-null  int64 \n",
            " 5   Recommended        23486 non-null  int64 \n",
            " 6   Positive Feedback  23486 non-null  int64 \n",
            " 7   Division           23472 non-null  object\n",
            " 8   Department         23472 non-null  object\n",
            " 9   Category           23472 non-null  object\n",
            "dtypes: int64(5), object(5)\n",
            "memory usage: 1.8+ MB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.describe"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eGsdApI0ObsW",
        "outputId": "218de486-36a4-4aff-c49b-7792dbacf073"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<bound method NDFrame.describe of        Clothing ID  Age                                              Title  \\\n",
              "0              767   33                                                NaN   \n",
              "1             1080   34                                                NaN   \n",
              "2             1077   60                            Some major design flaws   \n",
              "3             1049   50                                   My favorite buy!   \n",
              "4              847   47                                   Flattering shirt   \n",
              "...            ...  ...                                                ...   \n",
              "23481         1104   34                     Great dress for many occasions   \n",
              "23482          862   48                         Wish it was made of cotton   \n",
              "23483         1104   31                              Cute, but see through   \n",
              "23484         1084   28  Very cute dress, perfect for summer parties an...   \n",
              "23485         1104   52                    Please make more like this one!   \n",
              "\n",
              "                                                  Review  Rating  Recommended  \\\n",
              "0      Absolutely wonderful - silky and sexy and comf...       4            1   \n",
              "1      Love this dress!  it's sooo pretty.  i happene...       5            1   \n",
              "2      I had such high hopes for this dress and reall...       3            0   \n",
              "3      I love, love, love this jumpsuit. it's fun, fl...       5            1   \n",
              "4      This shirt is very flattering to all due to th...       5            1   \n",
              "...                                                  ...     ...          ...   \n",
              "23481  I was very happy to snag this dress at such a ...       5            1   \n",
              "23482  It reminds me of maternity clothes. soft, stre...       3            1   \n",
              "23483  This fit well, but the top was very see throug...       3            0   \n",
              "23484  I bought this dress for a wedding i have this ...       3            1   \n",
              "23485  This dress in a lovely platinum is feminine an...       5            1   \n",
              "\n",
              "       Positive Feedback        Division Department   Category  \n",
              "0                      0       Initmates   Intimate  Intimates  \n",
              "1                      4         General    Dresses    Dresses  \n",
              "2                      0         General    Dresses    Dresses  \n",
              "3                      0  General Petite    Bottoms      Pants  \n",
              "4                      6         General       Tops    Blouses  \n",
              "...                  ...             ...        ...        ...  \n",
              "23481                  0  General Petite    Dresses    Dresses  \n",
              "23482                  0  General Petite       Tops      Knits  \n",
              "23483                  1  General Petite    Dresses    Dresses  \n",
              "23484                  2         General    Dresses    Dresses  \n",
              "23485                 22  General Petite    Dresses    Dresses  \n",
              "\n",
              "[23486 rows x 10 columns]>"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4MTax40UObtn",
        "outputId": "42870e21-0532-4ff1-a7ac-268edc1ca7e1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(23486, 10)"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.isna().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "folGqYraObyi",
        "outputId": "7b54e779-1c9f-4c3b-9a51-f9da50753430"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Clothing ID             0\n",
              "Age                     0\n",
              "Title                3810\n",
              "Review                845\n",
              "Rating                  0\n",
              "Recommended             0\n",
              "Positive Feedback       0\n",
              "Division               14\n",
              "Department             14\n",
              "Category               14\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df[df['Review']==\"\"]= np.NaN"
      ],
      "metadata": {
        "id": "XZikWadYObzy"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df['Review'].fillna(\"No Review\", inplace = True)"
      ],
      "metadata": {
        "id": "cK6EQL7QOb4x"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.isna().sum()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qv2bdHMXOb5_",
        "outputId": "33133b15-cb3e-4710-8c95-10e12f3e287e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Clothing ID             0\n",
              "Age                     0\n",
              "Title                3810\n",
              "Review                  0\n",
              "Rating                  0\n",
              "Recommended             0\n",
              "Positive Feedback       0\n",
              "Division               14\n",
              "Department             14\n",
              "Category               14\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['Review']"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rValzar5Ob_A",
        "outputId": "1710f49c-cf4a-4716-fe91-9f25f7b2308d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0        Absolutely wonderful - silky and sexy and comf...\n",
              "1        Love this dress!  it's sooo pretty.  i happene...\n",
              "2        I had such high hopes for this dress and reall...\n",
              "3        I love, love, love this jumpsuit. it's fun, fl...\n",
              "4        This shirt is very flattering to all due to th...\n",
              "                               ...                        \n",
              "23481    I was very happy to snag this dress at such a ...\n",
              "23482    It reminds me of maternity clothes. soft, stre...\n",
              "23483    This fit well, but the top was very see throug...\n",
              "23484    I bought this dress for a wedding i have this ...\n",
              "23485    This dress in a lovely platinum is feminine an...\n",
              "Name: Review, Length: 23486, dtype: object"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.columns\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fuXO_-bbOcAQ",
        "outputId": "d6d3c196-e19f-4753-9476-b078bc87181a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['Clothing ID', 'Age', 'Title', 'Review', 'Rating', 'Recommended',\n",
              "       'Positive Feedback', 'Division', 'Department', 'Category'],\n",
              "      dtype='object')"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Data Visualization**"
      ],
      "metadata": {
        "id": "fkLv6n9KyGDA"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Distribution of Ratings\n",
        "plt.figure(figsize=(8, 6))\n",
        "sns.countplot(x='Rating', data=df)\n",
        "plt.title('Distribution of Ratings')\n",
        "plt.xlabel('Rating')\n",
        "plt.ylabel('Count')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 500
        },
        "id": "CVD50thbyX5R",
        "outputId": "ab7da18b-39e1-40d7-ae6d-74b7f0691420"
      },
      "execution_count": 61,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 800x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAskAAAIjCAYAAADx6oYJAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAABAxUlEQVR4nO3de1hVZd7/8c9GBDwBHkEKkdTxiHioDCsPE4lGBxqb0vI4qFmeMWMoM9SZLB1PpebTU0pTNqX9iho1FTE1k0wx8lBaFkYlYHnaiooC6/fHPKxx33gkcCO9X9e1rot1r+9e67t2XtuPq3vfOCzLsgQAAADA5uHuBgAAAICKhpAMAAAAGAjJAAAAgIGQDAAAABgIyQAAAICBkAwAAAAYCMkAAACAgZAMAAAAGAjJAAAAgIGQDKDSS0xMlMPhuCrX6tatm7p162bvr1+/Xg6HQ+++++5Vuf6gQYPUuHHjq3Kt0jpx4oSGDBmiwMBAORwOjR071t0t2RwOhxITE93dBoAKgJAM4JqSlJQkh8Nhbz4+PgoKClJUVJRefPFFHT9+vEyuc+DAASUmJiojI6NMzleWKnJvl+O5555TUlKSHnvsMb3xxhvq37//BWsbN27s8t+7Ro0auvnmm/XPf/6z1NdfuXIlQRjAJTksy7Lc3QQAXK6kpCQNHjxYU6ZMUWhoqM6ePaucnBytX79eKSkpatSokT788EO1bdvWfk1BQYEKCgrk4+Nz2dfZtm2bbrrpJi1evFiDBg267NedOXNGkuTl5SXpP0+Su3fvrmXLlumBBx647POUtrezZ8+qqKhI3t7eZXKt8nDLLbfI09NTmzZtumRt48aNVbt2bY0fP16SlJ2drVdffVXffPONXnnlFQ0dOvSKrz9y5EjNnz9f5/vr7/Tp0/L09JSnp+cVnxdA5cKnAIBrUq9evXTjjTfa+wkJCVq3bp3uvvtu3Xvvvfr6669VrVo1SboqoefkyZOqXr26HY7dpWrVqm69/uU4ePCgWrVqddn11113nfr162fvDxo0SDfccINmz55dqpB8MVfyDykAlRvTLQBUGn/84x/1zDPP6IcfftCbb75pj59vTnJKSopuu+02+fv7q2bNmmrevLmeeuopSf95+nvTTTdJkgYPHmz/r/6kpCRJ/5l33KZNG6Wnp6tLly6qXr26/VpzTnKxwsJCPfXUUwoMDFSNGjV077336scff3Spady48XmfWp97zkv1dr45yXl5eRo/fryCg4Pl7e2t5s2b6x//+EeJJ6kOh0MjR45UcnKy2rRpI29vb7Vu3VqrVq06/xtuOHjwoGJjYxUQECAfHx+Fh4fr9ddft48Xz8/OzMzUihUr7N73799/WecvVr9+fbVo0ULfffedy/gnn3yiP//5z2rUqJG8vb0VHByscePG6dSpU3bNoEGDNH/+fPt+i7dz34Nzp2IU/9nZt2+fBg0aJH9/f/n5+Wnw4ME6efKky/VPnTql0aNHq169eqpVq5buvfde/fzzzyXOefz4cY0dO1aNGzeWt7e3GjRooDvvvFPbt2+/ovcBQPniSTKASqV///566qmntGbNmgs+Zdy9e7fuvvtutW3bVlOmTJG3t7f27dunTz/9VJLUsmVLTZkyRZMmTdKwYcN0++23S5I6d+5sn+PQoUPq1auX+vTpo379+ikgIOCiff3973+Xw+FQfHy8Dh48qDlz5igyMlIZGRn2E+/LcTm9ncuyLN177736+OOPFRsbq3bt2mn16tWaMGGCfv75Z82ePdulftOmTXrvvff0+OOPq1atWnrxxRfVu3dvZWVlqW7duhfs69SpU+rWrZv27dunkSNHKjQ0VMuWLdOgQYN09OhRjRkzRi1bttQbb7yhcePG6frrr7enUNSvX/+y71/6z/SZn376SbVr13YZX7ZsmU6ePKnHHntMdevW1eeff66XXnpJP/30k5YtWyZJevTRR3XgwAGlpKTojTfeuOxrPvjggwoNDdW0adO0fft2vfrqq2rQoIFeeOEFu2bQoEFaunSp+vfvr1tuuUUbNmxQdHR0iXMNHz5c7777rkaOHKlWrVrp0KFD2rRpk77++mt16NDhit4LAOXIAoBryOLFiy1J1tatWy9Y4+fnZ7Vv397ef/bZZ61zP+5mz55tSbJ++eWXC55j69atliRr8eLFJY517drVkmQtXLjwvMe6du1q73/88ceWJOu6666znE6nPb506VJLkjV37lx7LCQkxBo4cOAlz3mx3gYOHGiFhITY+8nJyZYk629/+5tL3QMPPGA5HA5r37599pgky8vLy2Xsyy+/tCRZL730UolrnWvOnDmWJOvNN9+0x86cOWNFRERYNWvWdLn3kJAQKzo6+qLnO7e2R48e1i+//GL98ssv1s6dO63+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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Age Distribution\n",
        "plt.figure(figsize=(8, 6))\n",
        "sns.histplot(df['Age'], bins=30, kde=True)\n",
        "plt.title('Age Distribution')\n",
        "plt.xlabel('Age')\n",
        "plt.ylabel('Count')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 506
        },
        "id": "Jkszo0f3ygYM",
        "outputId": "7a2b5ef1-dab4-4b53-dd63-030dc399df1b"
      },
      "execution_count": 62,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 800x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAsAAAAIjCAYAAAAN/63DAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAAB1hUlEQVR4nO3deXhTVf4G8PdmT5d0X+lKgbbsq1hRQUFQ0XHBUREU9w3ccNx+7joOo46OzgzKLCrOiOIy6CguiGyKVPYChVKgFFq6km7plqRJzu+P0kihQJe0N8l9P8+TB3Lvyc33XgJ9OTn3HEkIIUBEREREpBAquQsgIiIiIupLDMBEREREpCgMwERERESkKAzARERERKQoDMBEREREpCgMwERERESkKAzARERERKQoDMBEREREpCgMwERERESkKAzAREQ+6tChQ5AkCYsXL+7191q8eDEkScKhQ4fc21JSUnDZZZf1+nsDwNq1ayFJEtauXdsn70dE/o0BmIgU7a233oIkSRg/frzcpUCSJPdDo9EgPDwcY8aMwQMPPIA9e/Z47H3eeuutPgnN3eHNtRGR/5CEEELuIoiI5DJhwgSUlpbi0KFD2L9/PwYMGCBbLZIk4aKLLsJNN90EIQTq6uqwY8cOfPrpp2hsbMTLL7+M+fPnu9sLIWCz2aDVaqFWqzv9PkOHDkVkZGSXelOdTidaWlqg1+shSRKA1h7goUOHYvny5Z0+Tndrc7lcsNvt0Ol0UKnYd0NEPcN/RYhIsQoLC7Fhwwa8/vrriIqKwpIlS+QuCYMGDcLs2bNx4403Yt68efjnP/+JgoICjBs3Dg8//DC++eYbd1tJkmAwGLoUfruqsbERAKBWq2EwGNzht6+pVCoYDAaGXyLyCP5LQkSKtWTJEoSFhWH69Om45pprThmAq6qqcOONN8JkMiE0NBRz5szBjh07Ohx/u3fvXlxzzTUIDw+HwWDA2LFj8eWXX/aozoiICCxduhQajQYvvfSSe3tHY4DLy8txyy23ICEhAXq9HnFxcbjiiivcY3dTUlKwe/durFu3zj3cYtKkSQB+Hee7bt063HvvvYiOjkZCQkK7fcePAW7z/fffY+TIkTAYDBg8eDCWLVvWbv9zzz3XYXA+8Zinq+1UY4A//fRTjBkzBkajEZGRkZg9ezZKSkratbn55psRFBSEkpISXHnllQgKCkJUVBR+97vfwel0nuHqE5E/0shdABGRXJYsWYKrr74aOp0OM2fOxNtvv43Nmzdj3Lhx7jYulwuXX345Nm3ahHvuuQcZGRn43//+hzlz5px0vN27d2PChAno168fHn/8cQQGBuKTTz7BlVdeif/+97+46qqrul1rUlISJk6ciDVr1sBiscBkMnXYbsaMGdi9ezfuu+8+pKSkoLKyEitXrkRRURFSUlLwxhtv4L777kNQUBCefPJJAEBMTEy7Y9x7772IiorCM8884+4BPpX9+/fjuuuuw9133405c+bgvffew29/+1t89913uOiii7p0jp2p7XiLFy/GLbfcgnHjxmHBggWoqKjAm2++iZ9//hnbt29HaGiou63T6cS0adMwfvx4/OlPf8IPP/yA1157DWlpabjnnnu6VCcR+QFBRKRAW7ZsEQDEypUrhRBCuFwukZCQIB544IF27f773/8KAOKNN95wb3M6neLCCy8UAMR7773n3j558mQxbNgwYbVa3dtcLpc455xzxMCBA89YEwAxd+7cU+5/4IEHBACxY8cOIYQQhYWF7WqoqakRAMSrr7562vcZMmSImDhx4knb33vvPQFAnHvuucLhcHS4r7Cw0L0tOTlZABD//e9/3dvq6upEXFycGDVqlHvbs88+Kzr6cdPRMU9V25o1awQAsWbNGiGEEHa7XURHR4uhQ4eK5uZmd7vly5cLAOKZZ55xb5szZ44AIF544YV2xxw1apQYM2bMSe9FRP6PQyCISJGWLFmCmJgYXHDBBQBax9Ned911WLp0abuvxb/77jtotVrccccd7m0qlQpz585td7zq6mqsXr0a1157Lerr62E2m2E2m1FVVYVp06Zh//79J30131VBQUEAgPr6+g73G41G6HQ6rF27FjU1Nd1+nzvuuKPT44rj4+Pb9WybTCbcdNNN2L59O8rLy7tdw5ls2bIFlZWVuPfee2EwGNzbp0+fjoyMDHz99dcnvebuu+9u9/y8887DwYMHe61GIvJeDMBEpDhOpxNLly7FBRdcgMLCQhw4cAAHDhzA+PHjUVFRgVWrVrnbHj58GHFxcQgICGh3jBNnizhw4ACEEHj66acRFRXV7vHss88CACorK3tUd0NDAwAgODi4w/16vR4vv/wyvv32W8TExOD888/HK6+80uUgmpqa2um2AwYMOGl876BBgwCgw/HCnnL48GEAQHp6+kn7MjIy3PvbGAwGREVFtdsWFhbWo/8oEJHv4hhgIlKc1atXo6ysDEuXLsXSpUtP2r9kyRJMnTq1S8d0uVwAgN/97neYNm1ah216OsVabm4u1Gr1aQPqgw8+iMsvvxxffPEFVqxYgaeffhoLFizA6tWrMWrUqE69j9Fo7FGdJzrVzBF9eQNab86UQUS+hwGYiBRnyZIliI6OxsKFC0/at2zZMnz++edYtGgRjEYjkpOTsWbNGjQ1NbXrBT5w4EC71/Xv3x8AoNVqMWXKFI/XXFRUhHXr1iErK+uUPcBt0tLS8PDDD+Phhx/G/v37MXLkSLz22mv44IMPAJw6kHZHW8/38cfct28fgNZZHYDWnlYAqK2tbXdj2om9tF2pLTk5GQCQn5+PCy+8sN2+/Px8934ioo5wCAQRKUpzczOWLVuGyy67DNdcc81Jj3nz5qG+vt49ddm0adPQ0tKCf/7zn+5juFyuk8JzdHQ0Jk2ahL///e8oKys76X2PHj3a7Zqrq6sxc+ZMOJ1O9+wIHWlqaoLVam23LS0tDcHBwbDZbO5tgYGBqK2t7XY9xystLcXnn3/ufm6xWPDvf/8bI0eORGxsrLsGAPjxxx/d7RobG/H++++fdLzO1jZ27FhER0dj0aJF7c7t22+/RV5eHqZPn97dUyIiBWAPMBEpypdffon6+nr85je/6XD/2Wef7V4U47rrrsOVV16Js846Cw8//DAOHDiAjIwMfPnll6iurgbQvsdy4cKFOPfcczFs2DDccccd6N+/PyoqKpCdnY0jR45gx44dZ6xv3759+OCDDyCEgMVica8E19DQgNdffx0XX3zxaV87efJkXHvttRg8eDA0Gg0+//xzVFRU4Prrr3e3GzNmDN5++238/ve/x4ABAxAdHX1SL2pnDRo0CLfddhs2b96MmJgYvPvuu6ioqMB7773nbjN16lQkJSXhtttuwyOPPAK1Wo13330XUVFRKCoqane8ztam1Wrx8ssv45ZbbsHEiRMxc+ZM9zRoKSkpeOihh7p1PkSkEDLPQkFE1Kcuv/xyYTAYRGNj4ynb3HzzzUKr1Qqz2SyEEOLo0aPihhtuEMHBwSIkJETcfPPN4ueffxYAxNKlS9u9tqCgQNx0000iNjZWaLVa0a9fP3HZZZeJzz777Iy1AXA/VCqVCA0NFaNGjRIPPPCA2L1790ntT5wGzWw2i7lz54qMjAwRGBgoQkJCxPjx48Unn3zS7nXl5eVi+vTpIjg4WABwTzvWNi3Z5s2bT3qvU02DNn36dLFixQoxfPhwodfrRUZGhvj0009Pev3WrVvF+PHjhU6nE0lJSeL111/v8Jinqu3EadDafPzxx2LUqFFCr9eL8PBwMWvWLHHkyJF2bebMmSMCAwNPqulU07MRkf+ThBBCnuhNROS7vvjiC1x11VVYv349JkyYIHc5RETUBQzARERn0Nzc3G5mBKfTialTp2LLli0oLy/3+KwJRETUuzgGmIjoDO677z40NzcjKysLNpsNy5Ytw4YNG/CHP/yB4ZeIyAexB5iI6Aw+/PBDvPbaazhw4ACsVisGDBiAe+65B/PmzZO7NCIi6gYGYCIiIiJSFM4DTERERESKwgBMRERERIrCm+A6weVyobS0FMHBwR5dQpSIiIiIPEMIgfr6esTHx0OlOn0fLwNwJ5SWliIxMVHuMoiIiIjoDIqLi5GQkHDaNgzAnRAcHAyg9YKaTCaZqyEiIiKiE1ksFiQmJrpz2+kwAHdC27AHk8nEAExERETkxTozXJU3wRERERGRojAAExEREZGiMAATERERkaIwABMRERGRojAAExEREZGiMAATERERkaIwABMRERGRojAAExEREZGiMAATERERkaIwABMRERGRojAAExEREZGiMAATERERkaIwABMRERGRojAAExEREZGiMAATERERkaIwABMRERGRojAAExEREZGiMAATERERkaJo5C6AiM6sqKgIZrPZI8eKjIxEUlKSR45FRETkixiAibxcUVERMjIz0dzU5JHjGQMCsDcvjyGYiIgUiwGYyMuZzWY0NzVh1mOvIiYprUfHqigqwJKXH4HZbGYAJiIixWIAJvIRMUlpSBg4RO4yiIiIfB5vgiMiIiIiRWEAJiIiIiJFYQAmIiIiIkVhACYiIiIiRWEAJiIiIiJFYQAmIiIiIkVhACYiIiIiRWEAJiIiIiJFYQAmIiIiIkVhACYiIiIiRWEAJiIiIiJFYQAmIiIiIkVhACYiIiIiRWEAJiIiIiJFYQAmIiIiIkVhACYiIiIiRWEAJiIiIiJFYQAmIiIiIkVhACYiIiIiRWEAJiIiIiJFYQAmIiIiIkVhACYiIiIiRWEAJiIiIiJFYQAmIiIiIkVhACYiIiIiRWEAJiIiIiJFYQAmIiIiIkVhACYiIiIiRWEAJiIiIiJFYQAmIiIiIkVhACYiIiIiRWEAJiIiIiJFYQAmIiIiIkVhACYiIiIiRWEAJiIiIiJFYQAmIiIiIkVhACYiIiIiRWEAJiIiIiJFYQAmIiIiIkVhACYiIiIiRWEAJiIiIiJFYQAmIiIiIkWRNQAvWLAA48aNQ3BwMKKjo3HllVciPz+/XZtJkyZBkqR2j7vvvrtdm6KiIkyfPh0BAQGIjo7GI488AofD0a7N2rVrMXr0aOj1egwYMACLFy/u7dMjIiIiIi8kawBet24d5s6di19++QUrV65ES0sLpk6disbGxnbt7rjjDpSVlbkfr7zyinuf0+nE9OnTYbfbsWHDBrz//vtYvHgxnnnmGXebwsJCTJ8+HRdccAFycnLw4IMP4vbbb8eKFSv67FyJiIiIyDto5Hzz7777rt3zxYsXIzo6Glu3bsX555/v3h4QEIDY2NgOj/H9999jz549+OGHHxATE4ORI0fixRdfxGOPPYbnnnsOOp0OixYtQmpqKl577TUAQGZmJtavX48///nPmDZtWu+dIBERERF5Ha8aA1xXVwcACA8Pb7d9yZIliIyMxNChQ/HEE0+gqanJvS87OxvDhg1DTEyMe9u0adNgsViwe/dud5spU6a0O+a0adOQnZ3dYR02mw0Wi6Xdg4iIiIj8g6w9wMdzuVx48MEHMWHCBAwdOtS9/YYbbkBycjLi4+Oxc+dOPPbYY8jPz8eyZcsAAOXl5e3CLwD38/Ly8tO2sVgsaG5uhtFobLdvwYIFeP755z1+jkREREQkP68JwHPnzkVubi7Wr1/fbvudd97p/v2wYcMQFxeHyZMno6CgAGlpab1SyxNPPIH58+e7n1ssFiQmJvbKexERERFR3/KKIRDz5s3D8uXLsWbNGiQkJJy27fjx4wEABw4cAADExsaioqKiXZu2523jhk/VxmQyndT7CwB6vR4mk6ndg4iIiIj8g6wBWAiBefPm4fPPP8fq1auRmpp6xtfk5OQAAOLi4gAAWVlZ2LVrFyorK91tVq5cCZPJhMGDB7vbrFq1qt1xVq5ciaysLA+dCRERERH5ClkD8Ny5c/HBBx/gww8/RHBwMMrLy1FeXo7m5mYAQEFBAV588UVs3boVhw4dwpdffombbroJ559/PoYPHw4AmDp1KgYPHowbb7wRO3bswIoVK/DUU09h7ty50Ov1AIC7774bBw8exKOPPoq9e/firbfewieffIKHHnpItnMnIiIiInnIGoDffvtt1NXVYdKkSYiLi3M/Pv74YwCATqfDDz/8gKlTpyIjIwMPP/wwZsyYga+++sp9DLVajeXLl0OtViMrKwuzZ8/GTTfdhBdeeMHdJjU1FV9//TVWrlyJESNG4LXXXsO//vUvToFGREREpECy3gQnhDjt/sTERKxbt+6Mx0lOTsY333xz2jaTJk3C9u3bu1QfEREREfkfr7gJjoiIiIiorzAAExEREZGiMAATERERkaIwABMRERGRojAAExEREZGiMAATERERkaIwABMRERGRojAAExEREZGiMAATERERkaIwABMRERGRojAAExEREZGiMAATERERkaIwABMRERGRojAAExEREZGiMAATERERkaIwABMRERGRojAAE/mJFqcLDqdL7jKIiIi8nkbuAoioe4QQ2FNmwa6SOliaHWhucUKjknD+wCgM7WeCJElyl0hEROSVGICJfFCz3YlVeytQcLSx3XaHS2B1fiWO1Dbhwoxo6DVqmSokIiLyXgzARD6mvM6K5TtL0Wh3QiUBZ/ePQEpEIIINGuwuteDnAjP2VTSgqsGO68YlQqvmSCciIqLjMQAT+ZByixWfby+B3elCWIAWFw+NRXSwwb1/THIY4kIM+HpXGaoa7dheVIuzUsNlrJiIiMj7sGuIyEfU2CR3+I0PNeD6cUntwm+b+FAjzhsYCQDYcrgajTZHX5dKRETk1RiAiXyALiYNP1VqYHe4EBdiwBUj+kGnOfVf3/SYYEQH69HiFPjlYFUfVkpEROT9GICJvFxhTQuir/s9WoSEuBADrhx5+vALAJLUOhsEAOwutcDcYOuLUomIiHwCAzCRF8srs+C5dVVQG4MRrnPhipHxZwy/bfqFGZEWFQgB4OcD5t4tlIiIyIcwABN5qdySOsz610bU2wVspfk4N9rR5WnNJgxoHQt8qKoJ9daW3iiTiIjI5zAAE3mhrYdrMPOfv6C60Y4B4VpUfPIMtN342xoWoEO/UCMAIL+i3sNVEhER+SYGYCIvs+GAGTe+sxH1VgfGpYThuYnhELbGM7/wFNJjgwEA+eUMwERERAADMJFXWZVXgZsXb0aT3YnzBkbi/VvPQkB3un6PMzA6CCoJ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AECj0eC6667DO++8494/bty4dq8566yz2j3fsWMHFi9ejKCgIPdj2rRpcLlcKCws7JsTISLqZRq5CyAiIs9455134HA42t30JoSAXq/H3/72t04do6GhAXfddRfuv//+k/YlJSV5rFYiIjkxABMR+QGHw4F///vfeO211zB16tR2+6688kp89NFHSE9PxzfffNNu3+bNm9s9Hz16NPbs2YMBAwb0es1ERHLhGGAiIj/wxRdf4LrrrkNlZSVCQkLa7XvsscewevVqfPLJJ0hPT8dDDz2E2267DTk5OXj44Ydx5MgR1NbWIiQkBDt37sTZZ5+NW2+9FbfffjsCAwOxZ88erFy5stO9yERE3o5jgImI/MA777yDKVOmnBR+AWDGjBnYsmUL6uvr8dlnn2HZsmUYPnw43n77bfcsEHq9HgAwfPhwrFu3Dvv27cN5552HUaNG4ZlnnuFcwkTkV9gDTESkYC+99BIWLVqE4uJiuUshIuozHANMRKQgb731FsaNG4eIiAj8/PPPePXVVznHLxEpDgMwEZGC7N+/H7///e9RXV2NpKQkPPzww3jiiSfkLouIqE9xCAQRERERKQpvgiMiIiIiRWEAJiIiIiJFYQAmIiIiIkVhACYiIiIiRWEAJiIiIiJFYQAmIiIiIkVhACYiIiIiRWEAJiIiIiJF+X+k9nk/l5VKqwAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Correlation Heatmap\n",
        "plt.figure(figsize=(10, 8))\n",
        "sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')\n",
        "plt.title('Correlation Heatmap')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 633
        },
        "id": "RzlixzBryjlB",
        "outputId": "c5a58f1d-32d4-461c-8da9-f83a70fd362d"
      },
      "execution_count": 63,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-63-c9babcf6d9e0>:3: FutureWarning: The default value of numeric_only in DataFrame.corr is deprecated. In a future version, it will default to False. Select only valid columns or specify the value of numeric_only to silence this warning.\n",
            "  sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x800 with 2 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAvwAAAKqCAYAAABGj4plAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAACl0klEQVR4nOzdd3hT5fvH8U+atulelJYpZcheCipD8auyUdyIoAwBtyJ1IipunIyfigtE+TpwgBMVkaEiU6AsKRtKgZYWukfaJvn90S/B0Da0IW1Ifb+u61wXefKcnPvk0PbOned5jsFms9kEAAAAoFby8XQAAAAAAKoPCT8AAABQi5HwAwAAALUYCT8AAABQi5HwAwAAALUYCT8AAABQi5HwAwAAALUYCT8AAABQi5HwAwAAALUYCT8Ar/Thhx/KYDBo//79bnvN/fv3y2Aw6MMPP3TbawIA4Gkk/ADs9uzZozvuuEPNmjVTQECAwsLC1LNnT82YMUMFBQWeDs9tPv30U02fPt3TYTgYNWqUQkJCKnzeYDDo3nvvrdYYZs6cyYcdAKiFfD0dAICzw8KFC3XjjTfKZDJpxIgRat++vYqKirRixQo9/PDD2rZtm9577z1Ph+kWn376qbZu3aoHHnjAob1JkyYqKCiQn5+fZwLzsJkzZyo6OlqjRo3ydCgAADci4Qegffv2aejQoWrSpImWLl2q+vXr25+75557tHv3bi1cuPCMj2Oz2VRYWKjAwMAyzxUWFsrf318+Pp774tFgMCggIMBjxwcAoDowpAeAXnnlFeXm5mr27NkOyf4JLVq00Pjx4+2PS0pK9Nxzz6l58+YymUyKi4vT448/LrPZ7LBfXFycrrzySi1atEhdu3ZVYGCg3n33XS1fvlwGg0Hz5s3TE088oYYNGyooKEjZ2dmSpDVr1qh///4KDw9XUFCQLr30Uv3555+nPY9vv/1WgwYNUoMGDWQymdS8eXM999xzslgs9j7/+c9/tHDhQh04cEAGg0EGg0FxcXGSKh7Dv3TpUl1yySUKDg5WRESErr76am3fvt2hz9NPPy2DwaDdu3dr1KhRioiIUHh4uEaPHq38/PzTxu4Ks9msyZMnq0WLFjKZTGrcuLEeeeSRMtdhzpw5uvzyyxUTEyOTyaS2bdvq7bffdugTFxenbdu26bfffrO/L//5z38knZwvsWLFCt1///2qW7euIiIidMcdd6ioqEiZmZkaMWKEIiMjFRkZqUceeUQ2m83h9V977TX16NFDderUUWBgoLp06aKvvvqqzDmdGLr0ySefqFWrVgoICFCXLl30+++/u/fNA4B/ESr8APT999+rWbNm6tGjR6X6jx07Vh999JFuuOEGPfjgg1qzZo2mTJmi7du36+uvv3bou2PHDt1888264447NG7cOLVq1cr+3HPPPSd/f3899NBDMpvN8vf319KlSzVgwAB16dJFkydPlo+Pjz1h/eOPP3ThhRdWGNeHH36okJAQxcfHKyQkREuXLtVTTz2l7Oxsvfrqq5KkSZMmKSsrS8nJyZo2bZokOR07/+uvv2rAgAFq1qyZnn76aRUUFOiNN95Qz549tWHDBvuHhROGDBmipk2basqUKdqwYYNmzZqlmJgYvfzyy5V6b9PT0yvVz2q1avDgwVqxYoVuv/12tWnTRlu2bNG0adO0c+dOffPNN/a+b7/9ttq1a6fBgwfL19dX33//ve6++25ZrVbdc889kqTp06frvvvuU0hIiCZNmiRJio2NdTjmfffdp3r16umZZ57R6tWr9d577ykiIkIrV67UOeecoxdffFE//vijXn31VbVv314jRoyw7ztjxgwNHjxYw4cPV1FRkebNm6cbb7xRP/zwgwYNGuRwnN9++02ff/657r//fplMJs2cOVP9+/fX2rVr1b59+0q9PwCAf7AB+FfLysqySbJdffXVleqfkJBgk2QbO3asQ/tDDz1kk2RbunSpva1JkyY2Sbaff/7Zoe+yZctskmzNmjWz5efn29utVqvt3HPPtfXr189mtVrt7fn5+bamTZva+vTpY2+bM2eOTZJt3759Dv1Odccdd9iCgoJshYWF9rZBgwbZmjRpUqbvvn37bJJsc+bMsbd17tzZFhMTYzt27Ji9bdOmTTYfHx/biBEj7G2TJ0+2SbLddtttDq957bXX2urUqVPmWKcaOXKkTZLT7Z577rH3/+9//2vz8fGx/fHHHw6v884779gk2f7880+n70u/fv1szZo1c2hr166d7dJLLy3T98R7fep16d69u81gMNjuvPNOe1tJSYmtUaNGZV7n1BiKiops7du3t11++eUO7SfO9a+//rK3HThwwBYQEGC79tpry8QGADg9hvQA/3InhtGEhoZWqv+PP/4oSYqPj3dof/DB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duzYoXfeeUc7d+6UJA0YMEDffPONcnNLv86666673BslAAAAUBHG8Dvl0sfyuLg4+5Ce7OxsffbZZ7rpppv0119/yWLh9tEAAADA2cLlj0O///67Ro4cqQYNGuj111/XZZddptWrV7szNgAAAABnqEoV/pSUFH344YeaPXu2srOzNWTIEJnNZn3zzTdq27ZtdcUIAAAAVMzJTWFRhQr/VVddpVatWmnz5s2aPn26Dh8+rDfeeKM6YwMAAABwhipd4f/pp590//3366677tK5555bnTEBAAAAlefDpF1nKv3urFixQjk5OerSpYsuuugivfnmm0pPT6/O2AAAAACcoUon/N26ddP777+vI0eO6I477tC8efPUoEEDWa1WLV68WDk55d9yHAAAAIDnVPn7j+DgYN12221asWKFtmzZogcffFAvvfSSYmJiNHjw4OqIEQAAAKiYweC5zQuc0YCnVq1a6ZVXXlFycrI+++wzd8UEAAAAwE3ccj9so9Goa665Rtdcc407Xg4AAACoPO606xTvDgAAAFCLuaXCDwAAAHgMy3I6xbsDAAAA1GIk/AAAAEAtxpAeAAAAeDcvWR7TU6jwAwAAALUYFX4AAAB4N5bldIp3BwAAAKjFSPgBAACAWowhPQAAAPBuTNp1igo/AAAAUItR4QcAAIB34067TvHuAAAAALUYFX4AAAB4NRtj+J2iwg8AAADUYiT8AAAAQC3GkB4AAAB4N+606xTvDgAAAFCLUeEHAACAd6PC7xTvDgAAAFCLkfADAAAAtRhDegAAAODVWIffOSr8AAAAQC1GhR8AAADejUm7TvHuAAAAALUYCT8AAAC8m8Hguc0Fb731luLi4hQQEKCLLrpIa9euddo/MzNT99xzj+rXry+TyaSWLVvqxx9/rPTxGNIDAAAA1JDPP/9c8fHxeuedd3TRRRdp+vTp6tevn3bs2KGYmJgy/YuKitSnTx/FxMToq6++UsOGDXXgwAFFRERU+pgk/AAAAEANmTp1qsaNG6fRo0dLkt555x0tXLhQH3zwgR577LEy/T/44AMdP35cK1eulJ+fnyQpLi6uSsdkSA8AAAC8m4+P57YqKCoq0vr169W7d+9/hO6j3r17a9WqVeXu891336l79+665557FBsbq/bt2+vFF1+UxWKp9HGp8AMAAAAuMpvNMpvNDm0mk0kmk6lM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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Data Preprocessing**"
      ],
      "metadata": {
        "id": "K8Q7NnKAyJ7H"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Handle Missing Values\n",
        "df['Title'].fillna(\"No Title\", inplace=True)  # Fill missing titles with \"No Title\"\n",
        "df['Review'].fillna(\"No Review\", inplace=True)  # Fill missing reviews with \"No Review\"\n"
      ],
      "metadata": {
        "id": "LCFJHe9dyvyS"
      },
      "execution_count": 64,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Drop rows with missing values in Division, Department, and Category\n",
        "df.dropna(subset=['Division', 'Department', 'Category'], inplace=True)\n"
      ],
      "metadata": {
        "id": "qMMA9TM3y31_"
      },
      "execution_count": 65,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Define Target Variable (y) and Feature Variables (X)**"
      ],
      "metadata": {
        "id": "llj1xDgTxsf0"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "y = df['Rating']"
      ],
      "metadata": {
        "id": "8sjipE4kOcFE"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X = df['Review']"
      ],
      "metadata": {
        "id": "S_I_PXlCOcGb"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df['Rating'].value_counts()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Z0-ZuDIlOcLN",
        "outputId": "deef9570-433f-4548-b1d3-6f85a431e218"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "5.0    13131\n",
              "4.0     5077\n",
              "3.0     2871\n",
              "2.0     1565\n",
              "1.0      842\n",
              "Name: Rating, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Train Test Split**"
      ],
      "metadata": {
        "id": "NJ4dF3D0xz8h"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import train_test_split"
      ],
      "metadata": {
        "id": "SgT0448lOcMe"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, stratify = y, random_state = 2529)"
      ],
      "metadata": {
        "id": "BoobwAxdOcRY"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X_train.shape, X_test.shape, y_train.shape, y_test.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JMpK3A3COcSw",
        "outputId": "b1b0c66a-c280-44f1-93eb-c03697ff8a47"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "((16440,), (7046,), (16440,), (7046,))"
            ]
          },
          "metadata": {},
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Modeling**"
      ],
      "metadata": {
        "id": "QNC2Mv0Dx5Uv"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.feature_extraction.text import CountVectorizer\n"
      ],
      "metadata": {
        "id": "UwR3d8QPOcX_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "cv = CountVectorizer(lowercase = True, analyzer = 'word', ngram_range=(2,3), stop_words = 'english', max_features=5000)"
      ],
      "metadata": {
        "id": "YcYZOnXTOcZa"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X_train  = cv.fit_transform(X_train)"
      ],
      "metadata": {
        "id": "_7hpp7v5Oce-"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "cv.get_feature_names_out()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "97HkdHnDOcgT",
        "outputId": "7f6d6de2-6b7c-47c2-b1fb-1b0166d10625"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['10 12', '10 bought', '10 fit', ..., 'yellow color', 'yoga pants',\n",
              "       'zipper little'], dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X_train.toarray()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RS8s-nrrU2ok",
        "outputId": "19924739-d7ff-4ab9-d400-a89b5dd33d9a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[0, 0, 0, ..., 0, 0, 0],\n",
              "       [0, 0, 0, ..., 0, 0, 0],\n",
              "       [0, 0, 0, ..., 0, 0, 0],\n",
              "       ...,\n",
              "       [0, 0, 0, ..., 0, 0, 0],\n",
              "       [0, 0, 0, ..., 0, 0, 0],\n",
              "       [0, 0, 0, ..., 0, 0, 0]])"
            ]
          },
          "metadata": {},
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X_test = cv.fit_transform(X_test)"
      ],
      "metadata": {
        "id": "xhVnUjnwU2yW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "cv.get_feature_names_out()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YltQ8Il1U2z7",
        "outputId": "7cf45c99-9963-4ce2-8d21-24f96c911b15"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['10 12', '10 dress', '10 fit', ..., 'years come', 'years old',\n",
              "       'yoga pants'], dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X_test.toarray()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CG2Yx2VdU24O",
        "outputId": "b84b6700-7872-49ed-c991-b2d647e47331"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[0, 0, 0, ..., 0, 0, 0],\n",
              "       [0, 0, 0, ..., 0, 0, 0],\n",
              "       [0, 0, 0, ..., 0, 0, 0],\n",
              "       ...,\n",
              "       [0, 0, 0, ..., 0, 0, 0],\n",
              "       [0, 0, 0, ..., 0, 0, 0],\n",
              "       [0, 0, 0, ..., 0, 0, 0]])"
            ]
          },
          "metadata": {},
          "execution_count": 29
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.naive_bayes import MultinomialNB"
      ],
      "metadata": {
        "id": "ZTnE4MDmU250"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model = MultinomialNB()"
      ],
      "metadata": {
        "id": "Ly-P2UTXU299"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model.fit(X_train, y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 75
        },
        "id": "xFXXmYGQVBvB",
        "outputId": "018cc302-043c-478f-8e60-7b7dd393bbcd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "MultinomialNB()"
            ],
            "text/html": [
              "<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>MultinomialNB()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">MultinomialNB</label><div class=\"sk-toggleable__content\"><pre>MultinomialNB()</pre></div></div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Model Evaluation**"
      ],
      "metadata": {
        "id": "O7aw62mUx--f"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred = model.predict(X_test)"
      ],
      "metadata": {
        "id": "xBblSAMMVBxD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qcCVUJB5VB0j",
        "outputId": "b5a91cd6-3d5d-4bba-a51b-684906251f2a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(7046,)"
            ]
          },
          "metadata": {},
          "execution_count": 34
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NroFPYb9VB2N",
        "outputId": "0f677d6d-e3e2-4590-f430-bc0c3ef93f28"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([1., 5., 5., ..., 5., 5., 5.])"
            ]
          },
          "metadata": {},
          "execution_count": 35
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "model.predict_proba(X_test)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EtuChkGoVB67",
        "outputId": "f45d414f-ad90-402b-b802-db08bf89adf6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[0.71118473, 0.02625165, 0.15465118, 0.01496876, 0.09294369],\n",
              "       [0.02416867, 0.04769471, 0.35268622, 0.16185007, 0.41360034],\n",
              "       [0.03582725, 0.06660584, 0.12226277, 0.21618005, 0.55912409],\n",
              "       ...,\n",
              "       [0.02320281, 0.08950939, 0.08962183, 0.16719203, 0.63047394],\n",
              "       [0.01167675, 0.00202714, 0.08539004, 0.34347398, 0.55743209],\n",
              "       [0.03959824, 0.05612822, 0.00688869, 0.1560574 , 0.74132745]])"
            ]
          },
          "metadata": {},
          "execution_count": 36
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import confusion_matrix, classification_report"
      ],
      "metadata": {
        "id": "QgcqWtGHVCCg"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(confusion_matrix(y_test, y_pred))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mhcX34ASVOCI",
        "outputId": "832eeb30-00ed-4318-843c-11067be51a64"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[  15   13   45   36  144]\n",
            " [  43   43   86   85  213]\n",
            " [ 116   78  113  166  388]\n",
            " [ 166  108  194  336  719]\n",
            " [ 371  272  349  722 2225]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(classification_report(y_test, y_pred))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qpovIFMMVOEE",
        "outputId": "18d93c8d-1a07-4c4a-fa11-2f940ff82b48"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "              precision    recall  f1-score   support\n",
            "\n",
            "         1.0       0.02      0.06      0.03       253\n",
            "         2.0       0.08      0.09      0.09       470\n",
            "         3.0       0.14      0.13      0.14       861\n",
            "         4.0       0.25      0.22      0.23      1523\n",
            "         5.0       0.60      0.56      0.58      3939\n",
            "\n",
            "    accuracy                           0.39      7046\n",
            "   macro avg       0.22      0.21      0.21      7046\n",
            "weighted avg       0.42      0.39      0.40      7046\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['Rating'].value_counts()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Uzbvk5tkVOLP",
        "outputId": "7f710a17-78f4-4134-c6e8-c6d2f2c6d655"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "5.0    13131\n",
              "4.0     5077\n",
              "3.0     2871\n",
              "2.0     1565\n",
              "1.0      842\n",
              "Name: Rating, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 40
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.replace({'Rating' : { 1:0, 2:0, 3:0, 4:1, 5:1}}, inplace = True)"
      ],
      "metadata": {
        "id": "0KFbPtygVOM6"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "y = df['Rating']"
      ],
      "metadata": {
        "id": "Vm99UPA3VOQ9"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X = df['Review']"
      ],
      "metadata": {
        "id": "Z5QZg1dAVOSn"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Prediction**"
      ],
      "metadata": {
        "id": "DU9Ixq6-zhyW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import train_test_split"
      ],
      "metadata": {
        "id": "D9Esp6NHVOWf"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, stratify = y, random_state = 2529)"
      ],
      "metadata": {
        "id": "SNIivCgwVOYN"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X_train.shape, X_test.shape, y_train.shape, y_test.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JyDhmTZ-VfwF",
        "outputId": "62f6d72e-6dc8-4681-8412-2024d2271e5b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "((16440,), (7046,), (16440,), (7046,))"
            ]
          },
          "metadata": {},
          "execution_count": 46
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.feature_extraction.text import CountVectorizer"
      ],
      "metadata": {
        "id": "RKwzNkG9Vfx2"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "cv = CountVectorizer(lowercase = True, analyzer = 'word', ngram_range=(2,3), stop_words = 'english', max_features=5000)"
      ],
      "metadata": {
        "id": "Gk7ir2zgVf1_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X_train  = cv.fit_transform(X_train)"
      ],
      "metadata": {
        "id": "c92RRwcrVf31"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X_test  = cv.fit_transform(X_test)"
      ],
      "metadata": {
        "id": "D8cPbroyVf8R"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.naive_bayes import MultinomialNB"
      ],
      "metadata": {
        "id": "zPe8l3mhVp04"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model = MultinomialNB()\n"
      ],
      "metadata": {
        "id": "-gtAIGQvVp3I"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model.fit(X_train, y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 75
        },
        "id": "zcU8WGuSVp5w",
        "outputId": "f7723e2c-4189-46a3-db0e-972d4e8b38ac"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "MultinomialNB()"
            ],
            "text/html": [
              "<style>#sk-container-id-2 {color: black;background-color: white;}#sk-container-id-2 pre{padding: 0;}#sk-container-id-2 div.sk-toggleable {background-color: white;}#sk-container-id-2 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-2 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-2 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-2 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-2 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-2 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-2 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-2 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-2 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-2 div.sk-item {position: relative;z-index: 1;}#sk-container-id-2 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-2 div.sk-item::before, #sk-container-id-2 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-2 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-2 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-2 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-2 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-2 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-2 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-2 div.sk-label-container {text-align: center;}#sk-container-id-2 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-2 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-2\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>MultinomialNB()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-2\" type=\"checkbox\" checked><label for=\"sk-estimator-id-2\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">MultinomialNB</label><div class=\"sk-toggleable__content\"><pre>MultinomialNB()</pre></div></div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 53
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import confusion_matrix, classification_report"
      ],
      "metadata": {
        "id": "t13XsZ8xVp7j"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(confusion_matrix(y_test, y_pred))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "o38bXPhbVp_8",
        "outputId": "3a0d1b28-a2e5-4fd4-dbac-3f818bdf2e3a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[   0  153  108  176  301  845]\n",
            " [   0  558  406  611 1044 2844]\n",
            " [   0    0    0    0    0    0]\n",
            " [   0    0    0    0    0    0]\n",
            " [   0    0    0    0    0    0]\n",
            " [   0    0    0    0    0    0]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(classification_report(y_test, y_pred))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nZsAtDvPVzsv",
        "outputId": "fa3cdb9f-5828-48b4-ced0-f849e55fe81a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "              precision    recall  f1-score   support\n",
            "\n",
            "         0.0       0.00      0.00      0.00      1583\n",
            "         1.0       0.78      0.10      0.18      5463\n",
            "         2.0       0.00      0.00      0.00         0\n",
            "         3.0       0.00      0.00      0.00         0\n",
            "         4.0       0.00      0.00      0.00         0\n",
            "         5.0       0.00      0.00      0.00         0\n",
            "\n",
            "    accuracy                           0.08      7046\n",
            "   macro avg       0.13      0.02      0.03      7046\n",
            "weighted avg       0.61      0.08      0.14      7046\n",
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/sklearn/metrics/_classification.py:1344: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n",
            "  _warn_prf(average, modifier, msg_start, len(result))\n",
            "/usr/local/lib/python3.10/dist-packages/sklearn/metrics/_classification.py:1344: UndefinedMetricWarning: Recall and F-score are ill-defined and being set to 0.0 in labels with no true samples. Use `zero_division` parameter to control this behavior.\n",
            "  _warn_prf(average, modifier, msg_start, len(result))\n",
            "/usr/local/lib/python3.10/dist-packages/sklearn/metrics/_classification.py:1344: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n",
            "  _warn_prf(average, modifier, msg_start, len(result))\n",
            "/usr/local/lib/python3.10/dist-packages/sklearn/metrics/_classification.py:1344: UndefinedMetricWarning: Recall and F-score are ill-defined and being set to 0.0 in labels with no true samples. Use `zero_division` parameter to control this behavior.\n",
            "  _warn_prf(average, modifier, msg_start, len(result))\n",
            "/usr/local/lib/python3.10/dist-packages/sklearn/metrics/_classification.py:1344: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n",
            "  _warn_prf(average, modifier, msg_start, len(result))\n",
            "/usr/local/lib/python3.10/dist-packages/sklearn/metrics/_classification.py:1344: UndefinedMetricWarning: Recall and F-score are ill-defined and being set to 0.0 in labels with no true samples. Use `zero_division` parameter to control this behavior.\n",
            "  _warn_prf(average, modifier, msg_start, len(result))\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred = model.predict(X_test)"
      ],
      "metadata": {
        "id": "NQRpFZKMVzvT"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BYv3aUQ7VzyH",
        "outputId": "d3b1e007-daf8-4cee-f0af-2dd5163ddfd8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(7046,)"
            ]
          },
          "metadata": {},
          "execution_count": 58
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "u24TIxJ7V6_7",
        "outputId": "0fb3d80c-6aea-4523-c396-3626d377d9c6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([1., 1., 1., ..., 1., 1., 1.])"
            ]
          },
          "metadata": {},
          "execution_count": 59
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Explarnation**\n",
        "The Multinomial Naive Bayes model was trained on the training set and then applied to the test set for predictions. The evaluation metrics, including the confusion matrix and classification report, are generated to assess the model's performance.\n",
        "\n",
        "**Confusion Matrix**:\n",
        "The confusion matrix provides a breakdown of the predicted and actual values:\n",
        "\n",
        "In the context of sentiment prediction:\n",
        "\n",
        "**True Positive (TP)**: Reviews correctly predicted as positive.\n",
        "True Negative (TN): Reviews correctly predicted as negative.\n",
        "False Positive (FP): Negative reviews incorrectly predicted as positive.\n",
        "False Negative (FN): Positive reviews incorrectly predicted as negative.\n",
        "Classification Report:\n",
        "The classification report includes precision, recall, and F1-score for each class, as well as the overall accuracy.\n",
        "\n",
        "Precision: The ability of the model not to label a negative sample as positive.\n",
        "Recall: The ability of the model to find all the positive samples.\n",
        "F1-Score: The weighted average of precision and recall.\n",
        "**Support:** The number of actual occurrences of the class in the specified dataset.\n",
        "These metrics provide a comprehensive overview of the model's performance in predicting the sentiment of women's clothing reviews."
      ],
      "metadata": {
        "id": "llRXxMocWHAD"
      }
    }
  ]
}

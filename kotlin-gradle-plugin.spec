Name:		kotlin-gradle-plugin
Version:	2.4.21
Release:	2
Summary:	Kotlin Gradle plugin
Group:		Development/Java
License:	Apache-2.0
URL:		https://github.com/JetBrains/kotlin
# Kotlin tag v2.4.21. org.jetbrains.kotlin:kotlin-gradle-plugin.
# Compiled with the installed kotlinc 2.0.21 against Gradle 8.11.1.
# The jar is the Gradle 8.11 variant. Android plugin sources are left out.
# semver4j is generated with antlr4 during the build. The TeamCity
# service-message parser, protobuf Kotlin extensions, and the Develocity
# agent adapters are compiled from source into this jar. They are not
# published as their own Maven coordinates.
# The jar name is versioned so it does not replace a kotlin-libs path.
Source0:	kotlin-gradle-plugin-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	java-21-openjdk-devel
BuildRequires:	kotlin = 2.0.21
BuildRequires:	python
BuildRequires:	sysjar
BuildRequires:	javapackages-filesystem
BuildRequires:	antlr4
BuildRequires:	antlr4-tool
BuildRequires:	gradle = 8.11.1
BuildRequires:	mvn(org.jetbrains.kotlin:kotlin-stdlib) = 2.4.21
BuildRequires:	mvn(org.jetbrains.kotlin:kotlin-reflect) = 2.4.21
BuildRequires:	mvn(org.jetbrains.kotlin:kotlin-script-runtime) = 2.4.21
BuildRequires:	mvn(org.jetbrains.kotlin:kotlin-compiler-embeddable) = 2.4.21
BuildRequires:	mvn(org.jetbrains.kotlin:kotlin-build-tools-api) = 2.4.21
BuildRequires:	mvn(org.jetbrains.kotlin:kotlin-build-tools-impl) = 2.4.21
BuildRequires:	mvn(org.jetbrains.kotlin:kotlin-compiler-runner) = 2.4.21
BuildRequires:	mvn(org.jetbrains.kotlin:kotlin-daemon-client) = 2.4.21
BuildRequires:	mvn(org.jetbrains.kotlin:kotlin-scripting-common) = 2.4.21
BuildRequires:	mvn(org.jetbrains.kotlin:kotlin-scripting-compiler-embeddable) = 2.4.21
BuildRequires:	mvn(org.jetbrains.kotlin:kotlin-scripting-jvm) = 2.4.21
BuildRequires:	mvn(org.jetbrains.kotlin:kotlin-gradle-plugin-api) = 2.4.21
BuildRequires:	mvn(org.jetbrains.kotlin:kotlin-gradle-plugin-annotations) = 2.4.21
BuildRequires:	mvn(org.jetbrains.kotlin:kotlin-tooling-core) = 2.4.21
BuildRequires:	mvn(org.jetbrains.kotlin:kotlin-metadata-jvm) = 2.4.21
BuildRequires:	mvn(org.jetbrains.kotlin:kotlin-time-instant) = 2.4.21
BuildRequires:	mvn(org.jetbrains.kotlinx:kotlinx-coroutines-core-jvm) = 1.10.2
BuildRequires:	mvn(org.jetbrains.kotlinx:kotlinx-serialization-core) = 1.13.0
BuildRequires:	mvn(org.jetbrains.kotlinx:kotlinx-serialization-json) = 1.13.0
BuildRequires:	mvn(com.android.tools.build:gradle-api) = 9.0.0
BuildRequires:	mvn(com.google.code.gson:gson)
BuildRequires:	mvn(com.google.guava:guava)
BuildRequires:	mvn(com.google.protobuf:protobuf-java)
BuildRequires:	mvn(com.google.code.findbugs:jsr305)
BuildRequires:	mvn(org.jetbrains:annotations)
BuildRequires:	mvn(org.antlr:antlr4-runtime)
BuildRequires:	mvn(org.bouncycastle:bcpg-jdk18on)
BuildRequires:	mvn(org.bouncycastle:bcprov-jdk18on)
BuildRequires:	mvn(org.bouncycastle:bcutil-jdk18on)
BuildRequires:	mvn(org.apache.commons:commons-compress)
BuildRequires:	mvn(org.slf4j:slf4j-api)
# gradle ships gradle-tooling-api-8.11.1.jar and does not Provide mvn(org.gradle:gradle-tooling-api).
Requires:	gradle = 8.11.1
Requires:	mvn(org.jetbrains.kotlin:kotlin-stdlib) = 2.4.21
Requires:	mvn(org.jetbrains.kotlin:kotlin-reflect) = 2.4.21
Requires:	mvn(org.jetbrains.kotlin:kotlin-script-runtime) = 2.4.21
Requires:	mvn(org.jetbrains.kotlin:kotlin-compiler-embeddable) = 2.4.21
Requires:	mvn(org.jetbrains.kotlin:kotlin-build-tools-api) = 2.4.21
Requires:	mvn(org.jetbrains.kotlin:kotlin-build-tools-impl) = 2.4.21
Requires:	mvn(org.jetbrains.kotlin:kotlin-compiler-runner) = 2.4.21
Requires:	mvn(org.jetbrains.kotlin:kotlin-daemon-client) = 2.4.21
Requires:	mvn(org.jetbrains.kotlin:kotlin-scripting-common) = 2.4.21
Requires:	mvn(org.jetbrains.kotlin:kotlin-scripting-compiler-embeddable) = 2.4.21
Requires:	mvn(org.jetbrains.kotlin:kotlin-scripting-jvm) = 2.4.21
Requires:	mvn(org.jetbrains.kotlin:kotlin-gradle-plugin-api) = 2.4.21
Requires:	mvn(org.jetbrains.kotlin:kotlin-gradle-plugin-annotations) = 2.4.21
Requires:	mvn(org.jetbrains.kotlin:kotlin-tooling-core) = 2.4.21
Requires:	mvn(org.jetbrains.kotlin:kotlin-metadata-jvm) = 2.4.21
Requires:	mvn(org.jetbrains.kotlin:kotlin-time-instant) = 2.4.21
Requires:	mvn(org.jetbrains.kotlinx:kotlinx-coroutines-core-jvm) = 1.10.2
Requires:	mvn(org.jetbrains.kotlinx:kotlinx-serialization-core) = 1.13.0
Requires:	mvn(org.jetbrains.kotlinx:kotlinx-serialization-json) = 1.13.0
Requires:	mvn(org.antlr:antlr4-runtime)
Requires:	mvn(com.google.code.gson:gson)
Requires:	mvn(com.google.guava:guava)
Requires:	mvn(com.google.protobuf:protobuf-java)
Requires:	mvn(org.jetbrains:annotations)
Requires:	mvn(org.bouncycastle:bcpg-jdk18on)
Requires:	mvn(org.bouncycastle:bcprov-jdk18on)
Requires:	mvn(org.bouncycastle:bcutil-jdk18on)
Requires:	mvn(org.apache.commons:commons-compress)
Requires:	mvn(org.slf4j:slf4j-api)

%description
org.jetbrains.kotlin:kotlin-gradle-plugin %{version}.
The Gradle 8.11 variant of the Kotlin Gradle plugin, compiled with kotlinc
2.0.21. Android plugin sources are not in this build.

%prep
%autosetup -n kotlin-gradle-plugin-%{version}
find . -type f \( -name '*.jar' -o -name '*.class' -o -name '*.so' -o -name '*.node' -o -name '*.wasm' \) -print > binaries.list
if [ -s binaries.list ]; then
	cat binaries.list
	exit 1
fi
test -s license/LICENSE.txt
test -s tools/compile_kgp.py
test -s vendor/semver4j/src/main/antlr4/com/github/gundy/semver4j/generated/grammar/NodeSemverVersion.g4
test -s vendor/teamcity-sm/jetbrains/buildServer/messages/serviceMessages/ServiceMessage.java
test -s src/libraries/tools/kotlin-gradle-plugin/src/common/kotlin/org/jetbrains/kotlin/gradle/internal/kapt/Kapt3KotlinGradleSubplugin.kt

%build
set -eo pipefail
export JAVA_HOME=%{_jvmdir}/java-21-openjdk
export PATH="$JAVA_HOME/bin:/usr/bin:/bin"
export KGP_JAR="$PWD/kotlin-gradle-plugin-%{version}.jar"
python tools/compile_kgp.py
test -s "$KGP_JAR"

cat > kotlin-gradle-plugin.pom << END
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>
  <groupId>org.jetbrains.kotlin</groupId>
  <artifactId>kotlin-gradle-plugin</artifactId>
  <version>%{version}</version>
  <name>kotlin-gradle-plugin</name>
  <description>Kotlin Gradle plugin.</description>
  <url>https://github.com/JetBrains/kotlin</url>
  <licenses>
    <license>
      <name>Apache-2.0</name>
      <url>https://www.apache.org/licenses/LICENSE-2.0.txt</url>
    </license>
  </licenses>
  <dependencies>
    <dependency>
      <groupId>org.jetbrains.kotlin</groupId>
      <artifactId>kotlin-stdlib</artifactId>
      <version>%{version}</version>
    </dependency>
    <dependency>
      <groupId>org.jetbrains.kotlin</groupId>
      <artifactId>kotlin-gradle-plugin-api</artifactId>
      <version>%{version}</version>
    </dependency>
    <dependency>
      <groupId>org.jetbrains.kotlin</groupId>
      <artifactId>kotlin-compiler-embeddable</artifactId>
      <version>%{version}</version>
    </dependency>
  </dependencies>
</project>
END

%install
set -eo pipefail
export JAVA_HOME=%{_jvmdir}/java-21-openjdk
export PATH="$JAVA_HOME/bin:/usr/bin:/bin"
mkdir -p %{buildroot}
sysjar install --buildroot %{buildroot} \
	--artifact kotlin-gradle-plugin.pom:kotlin-gradle-plugin-%{version}.jar \
	--file-name kotlin-gradle-plugin-%{version} \
	--filelist .mfiles
idx="%{buildroot}/usr/share/sysjar/index/org.jetbrains.kotlin/kotlin-gradle-plugin.sysjar"
moved="%{buildroot}/usr/share/sysjar/index/org.jetbrains.kotlin/kotlin-gradle-plugin-%{version}.sysjar"
test -s "$idx"
grep -F -q '"version": "%{version}"' "$idx"
grep -F -q '"artifactId": "kotlin-gradle-plugin"' "$idx"
/bin/mv "$idx" "$moved"
cat > .mfiles << EOF
%%dir /usr/share/sysjar/index/org.jetbrains.kotlin
/usr/share/sysjar/index/org.jetbrains.kotlin/kotlin-gradle-plugin-%{version}.sysjar
%{_javadir}/kotlin-gradle-plugin-%{version}.jar
/usr/share/maven-poms/kotlin-gradle-plugin-%{version}.pom
EOF
test -s %{buildroot}%{_javadir}/kotlin-gradle-plugin-%{version}.jar
if [ -e %{buildroot}%{_javadir}/kotlin-gradle-plugin.jar ]; then
	exit 1
fi

%check
set -eo pipefail
export JAVA_HOME=%{_jvmdir}/java-21-openjdk
export PATH="$JAVA_HOME/bin:/usr/bin:/bin"
JAR=%{buildroot}%{_javadir}/kotlin-gradle-plugin-%{version}.jar
STDLIB=%{_javadir}/kotlin-stdlib-%{version}.jar
KCE=%{_javadir}/kotlin-compiler-embeddable-%{version}.jar
test -s "$JAR"
test -s "$STDLIB"
test -s "$KCE"
mkdir -p check/out
cat > check/KgpCheck.java << 'EOF'
public class KgpCheck {
    public static void main(String[] args) {
        String name = org.jetbrains.kotlin.gradle.internal.Kapt3KotlinGradleSubpluginKt.getKaptTaskName("compileKotlin", "kaptGenerateStubs");
        if (!"kaptGenerateStubsKotlin".equals(name)) {
            throw new AssertionError(name);
        }
        String custom = org.jetbrains.kotlin.gradle.internal.Kapt3KotlinGradleSubpluginKt.getKaptTaskName("customCompile", "kapt");
        if (!"kaptCustomCompile".equals(custom)) {
            throw new AssertionError(custom);
        }
        System.out.println("kgp_ok " + name + " " + custom);
    }
}
EOF
javac -cp "$JAR:$STDLIB:$KCE" -d check/out check/KgpCheck.java
java -cp "check/out:$JAR:$STDLIB:$KCE" KgpCheck > check/out.txt
cat check/out.txt
grep -F -qx 'kgp_ok kaptGenerateStubsKotlin kaptCustomCompile' check/out.txt

%files -f .mfiles
%license license/LICENSE.txt license/semver4j-LICENSE.md license/protobuf-LICENSE license/develocity-adapters-LICENSE vendor/teamcity-sm/LICENSE
%doc license/NOTICE.txt
